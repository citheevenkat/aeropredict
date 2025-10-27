#!/usr/bin/env python3
"""
AeroPredict Configuration Management
Centralizes all configuration settings for easy customization
"""

import os
from datetime import datetime

class Config:
    """Configuration class for AeroPredict system"""

    # Application Info
    APP_NAME = "AeroPredict"
    VERSION = "1.0.0"
    DESCRIPTION = "AI-Powered Predictive Maintenance for Aviation"

    # Paths
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DATA_DIR = BASE_DIR
    DB_NAME = os.path.join(BASE_DIR, "aeropredict.db")
    NASA_CSV = os.path.join(BASE_DIR, "nasa_cmapss_train.csv")

    # Database Settings
    DB_ECHO = False  # Set to True for SQL query logging

    # NASA Dataset Parameters
    NUM_ENGINES = 100  # Number of engines to simulate
    MIN_CYCLES = 150   # Minimum cycles per engine
    MAX_CYCLES = 350   # Maximum cycles per engine
    RANDOM_SEED = 42   # For reproducible results

    # Sensor Thresholds (for anomaly detection)
    TEMP_NORMAL_MAX = 1700  # °F
    TEMP_WARNING_MAX = 1800
    TEMP_CRITICAL_MAX = 1850

    VIBRATION_NORMAL_MAX = 4.0  # mm/s
    VIBRATION_WARNING_MAX = 6.0
    VIBRATION_CRITICAL_MAX = 8.0

    # Health Score Thresholds
    HEALTH_CRITICAL = 50  # Below this = critical
    HEALTH_WARNING = 70   # Below this = warning
    HEALTH_GOOD = 90      # Above this = good

    # Failure Risk Thresholds
    RISK_LOW = 30      # Below this = low risk
    RISK_MEDIUM = 70   # Below this = medium risk
    RISK_HIGH = 100    # Above medium = high risk

    # Cost Parameters (in USD)
    PREDICTIVE_LABOR_COST = 2300
    PREDICTIVE_PARTS_COST = 4200
    PREDICTIVE_DOWNTIME_HOURS = 6

    REACTIVE_LABOR_COST = 18000
    REACTIVE_PARTS_COST = 12600
    REACTIVE_DOWNTIME_HOURS = 48
    REACTIVE_FLIGHT_CANCELLATIONS = 3
    COST_PER_CANCELLATION = 2000

    # Calculate total costs
    TOTAL_PREDICTIVE_COST = PREDICTIVE_LABOR_COST + PREDICTIVE_PARTS_COST
    TOTAL_REACTIVE_COST = (REACTIVE_LABOR_COST +
                          REACTIVE_PARTS_COST +
                          (REACTIVE_FLIGHT_CANCELLATIONS * COST_PER_CANCELLATION))

    # Supplier Settings
    DEFAULT_SUPPLIERS = [
        {
            "id": "SUP-001",
            "name": "GE Aviation Parts",
            "location": "Cincinnati, OH",
            "rating": 4.8,
            "avg_delivery_days": 5,
            "reliability": 0.98
        },
        {
            "id": "SUP-002",
            "name": "Pratt & Whitney Supply",
            "location": "Hartford, CT",
            "rating": 4.7,
            "avg_delivery_days": 6,
            "reliability": 0.96
        },
        {
            "id": "SUP-003",
            "name": "Rolls-Royce Components",
            "location": "Derby, UK",
            "rating": 4.9,
            "avg_delivery_days": 7,
            "reliability": 0.99
        },
        {
            "id": "SUP-004",
            "name": "AAR Corp",
            "location": "Wood Dale, IL",
            "rating": 4.5,
            "avg_delivery_days": 4,
            "reliability": 0.94
        },
        {
            "id": "SUP-005",
            "name": "Honeywell Aerospace",
            "location": "Phoenix, AZ",
            "rating": 4.6,
            "avg_delivery_days": 5,
            "reliability": 0.95
        }
    ]

    # Parts Catalog
    DEFAULT_PARTS = [
        {
            "part_number": "HPT-8472-A",
            "name": "High-Pressure Turbine Blade Assembly",
            "category": "Engine Core",
            "standard_price": 4200,
            "rush_price": 12600,
            "lead_time_days": 5,
            "stock": 15
        },
        {
            "part_number": "FAN-3392-B",
            "name": "Fan Blade Set (24 blades)",
            "category": "Fan Module",
            "standard_price": 8500,
            "rush_price": 25500,
            "lead_time_days": 7,
            "stock": 8
        },
        {
            "part_number": "BEAR-7721-C",
            "name": "Main Shaft Bearing",
            "category": "Engine Core",
            "standard_price": 3200,
            "rush_price": 9600,
            "lead_time_days": 4,
            "stock": 12
        },
        {
            "part_number": "SEAL-4432-D",
            "name": "Combustion Chamber Seal Kit",
            "category": "Combustion",
            "standard_price": 850,
            "rush_price": 2550,
            "lead_time_days": 2,
            "stock": 45
        },
        {
            "part_number": "FUEL-8821-E",
            "name": "Fuel Nozzle Assembly",
            "category": "Fuel System",
            "standard_price": 1200,
            "rush_price": 3600,
            "lead_time_days": 3,
            "stock": 30
        },
        {
            "part_number": "IGN-2234-F",
            "name": "Ignition System Complete",
            "category": "Ignition",
            "standard_price": 2800,
            "rush_price": 8400,
            "lead_time_days": 6,
            "stock": 10
        },
        {
            "part_number": "COMP-5543-G",
            "name": "Compressor Blade Stage 1",
            "category": "Compressor",
            "standard_price": 5200,
            "rush_price": 15600,
            "lead_time_days": 8,
            "stock": 6
        },
        {
            "part_number": "COOL-6654-H",
            "name": "Cooling Air Manifold",
            "category": "Cooling",
            "standard_price": 1800,
            "rush_price": 5400,
            "lead_time_days": 4,
            "stock": 18
        }
    ]

    # Aircraft Fleet Default Data
    DEFAULT_AIRCRAFT = [
        {
            "id": "A320-001",
            "model": "A320-200",
            "manufacturer": "Airbus",
            "year": 2018,
            "hours": 12340,
            "status": "Operational"
        },
        {
            "id": "A320-002",
            "model": "A320-200",
            "manufacturer": "Airbus",
            "year": 2019,
            "hours": 8420,
            "status": "Operational"
        },
        {
            "id": "A320-003",
            "model": "A320-200",
            "manufacturer": "Airbus",
            "year": 2020,
            "hours": 6200,
            "status": "Operational"
        },
        {
            "id": "A320-004",
            "model": "A320-200",
            "manufacturer": "Airbus",
            "year": 2019,
            "hours": 10100,
            "status": "Operational"
        },
        {
            "id": "B737-001",
            "model": "737-800",
            "manufacturer": "Boeing",
            "year": 2017,
            "hours": 15680,
            "status": "Maintenance"
        }
    ]

    # ML Model Parameters
    ML_TRAIN_TEST_SPLIT = 0.8
    ML_RANDOM_STATE = 42
    ML_N_ESTIMATORS = 100  # For Random Forest
    ML_MAX_DEPTH = 10

    # API Settings (for future REST API)
    API_HOST = "0.0.0.0"
    API_PORT = 5000
    API_DEBUG = False

    # Logging
    LOG_LEVEL = "INFO"  # DEBUG, INFO, WARNING, ERROR, CRITICAL
    LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

    @classmethod
    def get_db_path(cls):
        """Get the database path"""
        return cls.DB_NAME

    @classmethod
    def get_nasa_csv_path(cls):
        """Get the NASA CSV path"""
        return cls.NASA_CSV

    @classmethod
    def calculate_savings(cls):
        """Calculate savings per incident"""
        return cls.TOTAL_REACTIVE_COST - cls.TOTAL_PREDICTIVE_COST

    @classmethod
    def calculate_savings_percentage(cls):
        """Calculate savings percentage"""
        return (cls.calculate_savings() / cls.TOTAL_REACTIVE_COST) * 100

    @classmethod
    def display_config(cls):
        """Display current configuration"""
        print("="*80)
        print(f"  {cls.APP_NAME} v{cls.VERSION}")
        print(f"  {cls.DESCRIPTION}")
        print("="*80)
        print(f"\nDatabase: {cls.DB_NAME}")
        print(f"NASA Data: {cls.NASA_CSV}")
        print(f"\nCost Savings per Incident:")
        print(f"  Reactive: ${cls.TOTAL_REACTIVE_COST:,}")
        print(f"  Predictive: ${cls.TOTAL_PREDICTIVE_COST:,}")
        print(f"  Savings: ${cls.calculate_savings():,} ({cls.calculate_savings_percentage():.1f}%)")
        print("="*80)


# Development Config (for testing)
class DevelopmentConfig(Config):
    """Development configuration with verbose logging"""
    DB_ECHO = True
    LOG_LEVEL = "DEBUG"
    API_DEBUG = True


# Production Config
class ProductionConfig(Config):
    """Production configuration with optimizations"""
    DB_ECHO = False
    LOG_LEVEL = "WARNING"
    API_DEBUG = False


# Select config based on environment
def get_config():
    """Get configuration based on environment variable"""
    env = os.getenv('AEROPREDICT_ENV', 'development').lower()

    if env == 'production':
        return ProductionConfig
    else:
        return DevelopmentConfig


if __name__ == "__main__":
    # Display config when run directly
    Config.display_config()
