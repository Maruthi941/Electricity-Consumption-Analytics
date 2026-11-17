import os

from src.data_generator import generate_data
from src.pipeline import run_pipeline
from src.spark_processing import process_electricity_data

if __name__ == "__main__":

    print("========================================")
    print(" ELECTRICITY CONSUMPTION ANALYTICS")
    print("========================================")

    os.makedirs("data/processed", exist_ok=True)
    os.makedirs("outputs", exist_ok=True)

    print("\nSTEP 1: Generating Dataset")
    generate_data()

    print("\nSTEP 2: Data Cleaning and Analysis")
    run_pipeline()

    print("\nSTEP 3: Big Data Processing using PySpark")
    process_electricity_data()

    print("\n========================================")
    print(" PROJECT COMPLETED SUCCESSFULLY!")
    print("========================================")