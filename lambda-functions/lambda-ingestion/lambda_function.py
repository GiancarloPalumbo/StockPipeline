import urllib.request
import json
from datetime import datetime
import boto3

API_KEY = "My-API-Key"
SYMBOL = "AAPL"
BUCKET_NAME = "My-Bucket-Name"

def fetch_stock_data():
    base_url = "https://www.alphavantage.co/query"
    
    query_params = (
        f"?function=TIME_SERIES_DAILY"
        f"&symbol={SYMBOL}"
        f"&apikey={API_KEY}"
    )
    
    full_url = base_url + query_params

    with urllib.request.urlopen(full_url) as response:
        data = response.read().decode("utf-8")
        return json.loads(data)


def upload_to_s3(data):
    s3 = boto3.client("s3")

    filename = f"raw/{SYMBOL}_{datetime.now().date()}.json"

    s3.put_object(
        Bucket=BUCKET_NAME,
        Key=filename,
        Body=json.dumps(data)
    )


def lambda_handler(event, context):
    try:
        data = fetch_stock_data()
        upload_to_s3(data)

        return {
            "statusCode": 200,
            "body": json.dumps("Stock data uploaded successfully!")
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps(f"Error: {str(e)}")
        }
