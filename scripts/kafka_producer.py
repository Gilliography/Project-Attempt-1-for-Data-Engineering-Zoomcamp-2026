from kafka import KafkaProducer
import json
import time
import random

producer = KafkaProducer(
    bootstrap_servers='kafka:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def produce():
    for _ in range(100):
        data = {
            "trip_distance": random.uniform(1, 10),
            "fare_amount": random.uniform(5, 50)
        }
        producer.send("taxi_trips", data)
        time.sleep(1)

if __name__ == "__main__":
    produce()