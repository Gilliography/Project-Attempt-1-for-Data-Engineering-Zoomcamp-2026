import pandas as pd
import psycopg2
from io import StringIO
import os

FILE = "/opt/airflow/data/transformed.csv"

PG_CONFIG = {
    "host": os.getenv("PG_HOST", "postgres"),
    "port": int(os.getenv("PG_PORT", 5432)),
    "dbname": os.getenv("PG_DB", "airflow"),
    "user": os.getenv("PG_USER", "airflow"),
    "password": os.getenv("PG_PASSWORD", "airflow"),
}

def load():
    print("Loading into Postgres...")

    # Validate file exists before connecting
    if not os.path.exists(FILE):
        raise FileNotFoundError(f"Expected file not found: {FILE}")

    df = pd.read_csv(FILE)

    # Ensure correct column types before inserting
    df["tpep_pickup_datetime"] = pd.to_datetime(df["tpep_pickup_datetime"])
    df["tpep_dropoff_datetime"] = pd.to_datetime(df["tpep_dropoff_datetime"])
    df["trip_distance"] = pd.to_numeric(df["trip_distance"], errors="coerce")
    df["fare_amount"] = pd.to_numeric(df["fare_amount"], errors="coerce")
    df = df.dropna()

    print(f"Rows to insert: {len(df)}")

    conn = psycopg2.connect(**PG_CONFIG)
    cur = conn.cursor()

    try:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS trips (
                pickup_time  TIMESTAMP,
                dropoff_time TIMESTAMP,
                trip_distance FLOAT,
                fare_amount   FLOAT
            )
        """)

        # Fast bulk load using COPY instead of row-by-row INSERT
        buffer = StringIO()
        df.to_csv(buffer, index=False, header=False)
        buffer.seek(0)

        cur.copy_from(
            buffer,
            "trips",
            sep=",",
            columns=("pickup_time", "dropoff_time", "trip_distance", "fare_amount")
        )

        conn.commit()
        print(f"Successfully inserted {len(df)} rows into trips.")

    except Exception as e:
        conn.rollback()
        print(f"Insert failed, transaction rolled back: {e}")
        raise

    finally:
        cur.close()
        conn.close()


if __name__ == "__main__":
    load()