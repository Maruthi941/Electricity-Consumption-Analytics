import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import os

def run_pipeline():

    print("\nLoading Electricity Dataset...")

    df = pd.read_csv("data/raw/electricity.csv")

    print("\nOriginal Dataset:")
    print(df.head())

    print("\nCleaning Data...")

    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)

    df["datetime"] = pd.to_datetime(df["datetime"])

    df["date"] = df["datetime"].dt.date
    df["hour"] = df["datetime"].dt.hour
    df["month"] = df["datetime"].dt.month

    print("\nCleaned Dataset:")
    print(df.head())

    print("\nDaily Consumption Analysis")

    daily = df.groupby("date")["global_active_power"].sum()

    print(daily)

    print("\nMonthly Consumption Analysis")

    monthly = df.groupby("month")["global_active_power"].sum()

    print(monthly)

    print("\nHourly Consumption Analysis")

    hourly = df.groupby("hour")["global_active_power"].mean()

    print(hourly)

    os.makedirs("data/processed", exist_ok=True)
    os.makedirs("outputs", exist_ok=True)

    df.to_csv(
        "data/processed/cleaned_electricity.csv",
        index=False
    )

    daily.to_csv("data/processed/daily_summary.csv")
    monthly.to_csv("data/processed/monthly_summary.csv")
    hourly.to_csv("data/processed/hourly_summary.csv")

    print("\nSaving Data into SQLite...")

    conn = sqlite3.connect("outputs/electricity_analytics.db")

    df.to_sql(
        "electricity_consumption",
        conn,
        if_exists="replace",
        index=False
    )

    conn.close()

    print("Database Created Successfully!")

    print("\nGenerating Graphs...")

    plt.figure(figsize=(10, 5))
    daily.plot()
    plt.title("Daily Electricity Consumption")
    plt.xlabel("Date")
    plt.ylabel("Consumption")
    plt.tight_layout()
    plt.savefig("outputs/daily_consumption.png")
    plt.close()

    plt.figure(figsize=(10, 5))
    hourly.plot(kind="bar")
    plt.title("Hourly Electricity Consumption")
    plt.xlabel("Hour")
    plt.ylabel("Average Consumption")
    plt.tight_layout()
    plt.savefig("outputs/hourly_consumption.png")
    plt.close()

    plt.figure(figsize=(10, 5))
    monthly.plot(kind="bar")
    plt.title("Monthly Electricity Consumption")
    plt.xlabel("Month")
    plt.ylabel("Consumption")
    plt.tight_layout()
    plt.savefig("outputs/monthly_consumption.png")
    plt.close()

    print("\nPROJECT COMPLETED SUCCESSFULLY!")
    print("Check the outputs folder for graphs and database.")