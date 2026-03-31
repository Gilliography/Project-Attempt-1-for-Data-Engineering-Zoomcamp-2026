import pandas as pd
import psycopg2

FILE = "/opt/airflow/data/transformed.csv"

def load():
    print("Loading into Postgres...")

    conn = psycopg2.connect(
        host="postgres",
        port=5432,
        dbname="airflow",
        user="airflow",
        password="airflow"
    )

    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS trips (
        pickup_time TIMESTAMP,
        dropoff_time TIMESTAMP,
        trip_distance FLOAT,
        fare_amount FLOAT
    )
    """)

    df = pd.read_csv(FILE)

    for _, row in df.iterrows():
        cur.execute(
            "INSERT INTO trips VALUES (%s, %s, %s, %s)",
            tuple(row)
        )

    conn.commit()
    cur.close()
    conn.close()

    print("Data loaded!")