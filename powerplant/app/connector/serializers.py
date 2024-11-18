from rest_framework import serializers


class PowerplantSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, max_length=100)
    type = serializers.ChoiceField(
        required=True, choices=['gasfired', 'turbojet', 'windturbine']
    )
    efficiency = serializers.FloatField(required=True)
    pmin = serializers.FloatField(required=True)
    pmax = serializers.FloatField(required=True)


class FuelsSerializer(serializers.Serializer):
    gas_euro_per_mwh = serializers.FloatField(required=True)
    kerosine_euro_per_mwh = serializers.FloatField(required=True)
    co2_euro_per_ton = serializers.FloatField(required=True)
    wind_percent = serializers.FloatField(required=True)

    def to_internal_value(self, data):
        # Map incoming JSON fields to our internal field names
        data = {
            'gas_euro_per_mwh': data.get('gas(euro/MWh)'),
            'kerosine_euro_per_mwh': data.get('kerosine(euro/MWh)'),
            'co2_euro_per_ton': data.get('co2(euro/ton)'),
            'wind_percent': data.get('wind(%)'),
        }
        return super().to_internal_value(data)


class ProductionPlanRequestSerializer(serializers.Serializer):
    load = serializers.FloatField(required=True)
    fuels = FuelsSerializer()
    powerplants = PowerplantSerializer(many=True)


class ProductionPlanResponseSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, max_length=100)
    p = serializers.DecimalField(
        required=True, max_digits=10, decimal_places=1
    )
