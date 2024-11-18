class CalculateProductionPlanOperations:
    def __init__(self, data):
        self.load = data.get('load')
        self.fuels = data.get('fuels')
        self.powerplants = data.get('powerplants')

    def calculate_production(self):
        production_plan = []

        # Sort the powerplants based on the cost of fuel (merit-order)
        powerplants_sorted = sorted(
            self.powerplants,
            key=lambda x: self.calculate_cost(x, self.fuels),
            reverse=False,
        )

        remaining_load = self.load

        # Iterate over sorted plants and allocate power to each
        for plant in powerplants_sorted:
            power_generated = 0.0  # Default power generated is 0.0

            if remaining_load > 0:
                if plant['type'] == 'windturbine':
                    # Wind power is generated based on wind percentage
                    power_generated = min(
                        remaining_load,
                        plant['pmax'] * (self.fuels['wind_percent'] / 100),
                    )
                else:
                    # For other types of plants, it's limited by Pmax
                    power_generated = min(remaining_load, plant['pmax'])

                # Ensure the power generated meets the Pmin requirement
                if 0 < power_generated < plant['pmin']:
                    power_generated = plant['pmin']

                remaining_load -= power_generated

            # Append the result for this plant
            production_plan.append(
                {'name': plant['name'], 'p': round(power_generated, 1)}
            )

        # If there is still remaining load,
        # check if it's possible to meet the demand
        if remaining_load > 0:
            raise Exception(
                'Unable to meet the required'
                ' load with the available powerplants.'
            )

        return production_plan

    def calculate_cost(self, plant, fuels):
        """
        Calculate the cost per MWh
        for a given plant based on the fuel type.
        """
        if plant['type'] == 'gasfired':
            return fuels['gas_euro_per_mwh'] / plant['efficiency']
        elif plant['type'] == 'turbojet':
            return fuels['kerosine_euro_per_mwh'] / plant['efficiency']
        else:
            return 0  # Wind turbines have zero fuel cost
