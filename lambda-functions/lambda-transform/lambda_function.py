import json
import boto3
import csv
from io import StringIO

BUCKET_NAME = "My-Bucket-Name"
RAW_PREFIX = "raw/"
PROCESSED_PREFIX = "processed/"

s3 = boto3.client("s3")


def get_latest_raw_file():
    response = s3.list_objects_v2(
        Bucket=BUCKET_NAME,
        Prefix=RAW_PREFIX
    )

    files = response.get("Contents", [])

    if not files:
        raise Exception("No raw files found.")

    # Get most recent file
    latest_file = sorted(files, key=lambda x: x["LastModified"], reverse=True)[0]
    return latest_file["Key"]


def transform_json_to_csv(json_data):
    time_series = json_data.get("Time Series (Daily)", {})

    output = StringIO()
    writer = csv.writer(output)

    # Write header
    writer.writerow(["date", "open", "high", "low", "close", "volume"])

    for date, values in time_series.items():
        writer.writerow([
            date,
            values["1. open"],
            values["2. high"],
            values["3. low"],
            values["4. close"],
            values["5. volume"]
        ])

    return output.getvalue()


def lambda_handler(event, context):
    try:
        latest_key = get_latest_raw_file()

        obj = s3.get_object(Bucket=BUCKET_NAME, Key=latest_key)
        json_data = json.loads(obj["Body"].read())

        csv_data = transform_json_to_csv(json_data)

        new_key = latest_key.replace("raw/", "processed/").replace(".json", ".csv")

        s3.put_object(
            Bucket=BUCKET_NAME,
            Key=new_key,
            Body=csv_data
        )

        return {
            "statusCode": 200,
            "body": json.dumps(f"Processed file saved as {new_key}")
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps(str(e))
        }

