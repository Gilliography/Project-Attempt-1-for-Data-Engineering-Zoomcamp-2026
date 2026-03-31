from kafka import KafkaConsumer
import json
import psycopg2

consumer = KafkaConsumer(
    'taxi_trips',
    bootstrap_servers='kafka:9092',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

conn = psycopg2.connect(
    host="postgres",
    dbname="airflow",
    user="airflow",
    password="airflow"
)

cur = conn.cursor()

for message in consumer:
    data = message.value
    cur.execute(
        "INSERT INTO trips (trip_distance, fare_amount) VALUES (%s, %s)",
        (data["trip_distance"], data["fare_amount"])
    )
    conn.commit()