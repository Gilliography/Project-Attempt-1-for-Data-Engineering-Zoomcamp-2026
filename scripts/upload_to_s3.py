import boto3

def upload():
    s3 = boto3.client(
        's3',
        aws_access_key_id='YOUR_KEY',
        aws_secret_access_key='YOUR_SECRET'
    )

    s3.upload_file(
        '/opt/airflow/data/transformed.csv',
        'your-bucket-name',
        'taxi/transformed.csv'
    )

    print("Uploaded to S3!")