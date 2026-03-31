import pandas as pd

INPUT = "/opt/airflow/data/yellow_tripdata.parquet"
OUTPUT = "/opt/airflow/data/transformed.csv"

def transform():
    print("Transforming data...")

    df = pd.read_parquet(INPUT)

    df = df[[
        "tpep_pickup_datetime",
        "tpep_dropoff_datetime",
        "trip_distance",
        "fare_amount"
    ]]

    df = df.dropna()

    df.to_csv(OUTPUT, index=False)

    print("Transformation complete!")