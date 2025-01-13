import json

def lambda_handler(event, context):
    """
    A basic AWS Lambda function for testing AWS CodePipeline integration.
    """
    print("AWS Lambda function invoked!")
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Hello, AWS CodePipeline and GitHub integration works!",
            "input": event
        })
    }
