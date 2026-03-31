import requests
import os

URL = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2026-01.parquet"
OUTPUT = "/opt/airflow/data/yellow_tripdata.parquet"

def extract():
    print("Downloading dataset...")

    os.makedirs("/opt/airflow/data", exist_ok=True)

    response = requests.get(URL)
    with open(OUTPUT, "wb") as f:
        f.write(response.content)

    print("Download complete!")