# Power Plant Production Plan API

Overview
This project implements an API to compute the optimal power distribution across a fleet of power plants to meet a given
electricity load. The distribution is calculated using the merit-order dispatch approach, which ensures the most
cost-efficient operation of the power plants while adhering to their technical and operational constraints.

## How It Works

The API receives a payload containing:

- Total load to be distributed across the power plants.
- Fuel prices and wind availability.
- Power plant specifications, including efficiency, minimum/maximum production limits, and type.
- The response provides a production plan specifying how much power each plant should produce to meet the demand.

## Features

- Implements the merit-order dispatch algorithm:
- Prioritizes power plants based on the cost per MWh of electricity.
- Considers wind turbines (if available) as zero-cost options.
- Ensures production remains within the minimum (Pmin) and maximum (Pmax) capacity constraints of each power plant.
- Produces a detailed production plan, ensuring the total load is met (if feasible).

## Installation and Setup

### Environment Configuration

#### Setting up Environment Variables

For local development, setting up environment variables is necessary. Copy the provided `.env.powerplant.sample` file to
create your own `.env.powerplant` file. Update the values according to your configuration.

#### Step 1: Copy the Sample Environment File

Copy the contents of `.env.powerplant.sample`:

```bash
cp .env.powerplant.sample .env.powerplant
```

#### Step 2: Update Environment Variables

Open the newly created .env.powerplant file and update the values based on your specific configuration.
This file contains essential settings for the Django and other environment-specific variables.

### Step 3: Create a Virtual Environment

Create and activate a virtual environment using:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

#### Install Requirements

Install the required packages:

```bash
cd powerplant
pip install -r requirements.txt
```

#### Step 4: To run the service using docker, use the following Docker Compose command:

To build the containers and images for the service, use the following Docker Compose command:

```bash
docker-compose build powerplant
```

To start the application, use the following Docker Compose command:

```bash
docker-compose up powerplant
```

### Access

#### Endpoint

POST /production-plan

- POST /production-plan 
The service will be accessible at *http://powerplant.localhost:8888/swagger/*
- Swagger schema is available at *http://powerplant.localhost:8888/schema/* 


## Pre-commit Checks

Ensure code quality and formatting by running pre-commit checks:

```bash
cd powerplant
pre-commit run --all-files
```

## Files

- **docker-compose.yml**: Docker Compose configuration file.
- **Dockerfile**: Docker configuration file for building the microservice image.
- **config/requirements.txt**: List of Python dependencies.
- **pre-commit-config.yaml**: Configuration file for pre-commit hooks.
- **pyproject.toml**: TOML configuration file for the project.
- **.env.powerplant.sample**: sample for environment variables