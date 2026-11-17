import pandas as pd
import numpy as np
import os

def generate_data():

    os.makedirs("data/raw", exist_ok=True)

    dates = pd.date_range(
        start="2025-01-01",
        periods=24 * 30,
        freq="h"
    )

    np.random.seed(42)

    data = {
        "datetime": dates,
        "global_active_power": np.random.uniform(0.2, 5.0, len(dates)),
        "voltage": np.random.uniform(220, 240, len(dates)),
        "global_intensity": np.random.uniform(1, 25, len(dates))
    }

    df = pd.DataFrame(data)

    df.to_csv("data/raw/electricity.csv", index=False)

    print("Electricity dataset generated successfully!")
    print(df.head())

if __name__ == "__main__":
    generate_data()