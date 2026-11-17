from pyspark.sql import SparkSession
from pyspark.sql.functions import col, hour, avg, max, min

def process_electricity_data():

    spark = SparkSession.builder \
        .appName("ElectricityConsumptionAnalytics") \
        .master("local[*]") \
        .config("spark.ui.enabled", "false") \
        .getOrCreate()

    print("\nSpark Session Started Successfully!")

    df = spark.read.csv(
        "data/raw/electricity.csv",
        header=True,
        inferSchema=True
    )

    print("\nElectricity Dataset:")
    df.show(10)

    print("\nDataset Structure:")
    df.printSchema()

    print("\nTotal Records:")
    print(df.count())

    print("\nAverage Electricity Consumption:")
    df.select(avg("global_active_power")).show()

    print("\nMaximum Electricity Consumption:")
    df.select(max("global_active_power")).show()

    print("\nMinimum Electricity Consumption:")
    df.select(min("global_active_power")).show()

    print("\nHourly Consumption Analysis:")

    df = df.withColumn(
        "hour",
        hour(col("datetime"))
    )

    hourly = df.groupBy("hour").agg(
        avg("global_active_power").alias("average_consumption")
    )

    hourly.orderBy("hour").show()

    hourly.toPandas().to_csv(
        "data/processed/spark_hourly_summary.csv",
        index=False
    )

    print("\nPySpark Processing Completed!")

    spark.stop()