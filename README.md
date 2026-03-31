# My_First_DAG
In my Project named My_First_Dag inside a repository named "Project-Attempt-1-for-Data-Engineering-Zoomcamp-2026", I decided to proceed with the New York Taxi pipeline taking advantage of data available on https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2026-01.parquet 
The platforms and Technologies I used in the project include:
-Airflow
-Kafka
-Pandas
-EC2
-Python
-Postgres

---

# 🚀 NYC Taxi Data Engineering Pipeline

A complete **end-to-end data engineering pipeline** built with
Apache Airflow, PostgreSQL, Apache Kafka, and Amazon S3, deployed on Amazon EC2.

---

# 📊 Project Overview

This project demonstrates a **production-style data pipeline** that:

* Extracts NYC Taxi data from a public dataset
* Transforms and cleans the data
* Loads structured data into PostgreSQL
* Streams real-time data using Kafka
* Stores processed data in S3 (data lake)
* Visualizes insights using dashboards

---

# 🧱 Architecture

```text
        +-------------+
        |   Kafka     |  (Streaming Data)
        +------+------+
               |
               v
+-------------+--------------+
|        Apache Airflow       |
|  (Orchestration & ETL DAG) |
+------+------+--------------+
       |     |
       v     v
 PostgreSQL   S3 (Data Lake)
       |
       v
   Metabase Dashboard
```

---

# 📁 Project Structure

```bash
nyc-taxi-etl/
│
├── dags/
│   └── taxi_etl_pipeline.py
│
├── scripts/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   ├── kafka_producer.py
│   └── kafka_consumer.py
│
├── data/                 # Ignored in Git
│
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── .env
└── README.md
```

---

# ⚙️ Tech Stack

| Component        | Tool           |
| ---------------- | -------------- |
| Orchestration    | Apache Airflow |
| Database         | PostgreSQL     |
| Streaming        | Apache Kafka   |
| Storage          | Amazon S3      |
| Visualization    | Metabase       |
| Containerization | Docker         |

---

# 🔄 Pipeline Workflow

## 1. Extract

* Downloads NYC taxi dataset (Parquet format)

## 2. Transform

* Selects relevant columns
* Cleans missing values
* Converts to CSV

## 3. Load

* Inserts data into PostgreSQL table (`trips`)

## 4. Upload

* Uploads processed data to S3 bucket

## 5. Streaming (Kafka)

* Produces simulated taxi events
* Consumes and inserts into database in real time

---

# 🚀 Getting Started (Local)

## 1️⃣ Clone the repo

```bash
git clone https://github.com/YOUR_USERNAME/My_First_DAG.git
cd My_First_DAG
```

---

## 2️⃣ Setup environment

```bash
echo "AIRFLOW_UID=50000" > .env
```

---

## 3️⃣ Build & run

```bash
docker compose up -d --build
```

---

## 4️⃣ Access services

| Service            | URL                                            |
| ------------------ | ---------------------------------------------- |
| Airflow            | [http://localhost:8080](http://localhost:8080) |
| Metabase           | [http://localhost:3000](http://localhost:3000) |
| Adminer (optional) | [http://localhost:8081](http://localhost:8081) |

---

## 🔑 Airflow Login

```text
Username: airflow
Password: airflow
```

---

# 📊 Running the Pipeline

1. Open Airflow UI
2. Enable DAG: `nyc_taxi_etl_pipeline`
3. Click **Trigger DAG**

---

# ☁️ Deployment (AWS EC2)

## 1️⃣ Launch EC2 instance

* Ubuntu 22.04
* t2.medium recommended

---

## 2️⃣ Install Docker

```bash
sudo apt update
sudo apt install docker.io docker-compose -y
sudo usermod -aG docker ubuntu
```

---

## 3️⃣ Clone and run

```bash
git clone https://github.com/YOUR_USERNAME/My_First_DAG.git
cd My_First_DAG
docker compose up -d --build
```

---

## 4️⃣ Configure AWS credentials

```bash
export AWS_ACCESS_KEY_ID=my_key
export AWS_SECRET_ACCESS_KEY=my_secret
export AWS_DEFAULT_REGION=us-east-1
export S3_BUCKET=your-bucket-name
```

---

# 📡 Kafka Streaming

### Start producer

```bash
docker exec -it airflow-worker python /opt/airflow/scripts/kafka_producer.py
```

### Start consumer

```bash
docker exec -it airflow-worker python /opt/airflow/scripts/kafka_consumer.py
```

---

# 📈 Dashboard (Metabase)

1. Open [http://localhost:3000](http://localhost:3000)
2. Connect PostgreSQL:

   * Host: `postgres`
   * DB: `airflow`
   * User: `airflow`

---

## Example Queries

```sql
SELECT COUNT(*) FROM trips;

SELECT AVG(fare_amount) FROM trips;

SELECT trip_distance, fare_amount FROM trips LIMIT 1000;
```

---

# 🧠 Key Features

* ✅ Batch ETL pipeline
* ✅ Real-time streaming (Kafka)
* ✅ Data lake integration (S3)
* ✅ Containerized deployment
* ✅ Cloud-ready architecture
* ✅ Scalable design

---

# ⚠️ Notes

* Large data files are excluded via `.gitignore`
* Data is stored in S3 instead of GitHub
* Ensure ports are open when deploying to EC2

---

# 🚀 Future Improvements

* Add dbt transformations
* Use BigQuery / Redshift
* Add CI/CD pipeline
* Implement data quality checks
* Use Terraform for infrastructure

---
Diagrams and Screenshots


# 👨‍💻 Author

**Gilbert Kiprotich**

---

# ⭐ If you like this project

Give it a ⭐ on GitHub!

---