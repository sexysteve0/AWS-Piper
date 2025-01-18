import boto3
import json
import os

def lambda_handler(event, context):
    try:
        message = {
            "status": "success",
            "message": "Hello from Lambda!",
            "input": event
        }
        return {
            "statusCode": 200,
            "body": json.dumps(message)
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
