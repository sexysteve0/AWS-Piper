
import json

def lambda_handler(event, context):
    """
    Sample Lambda function to demonstrate CI/CD using CodeDeploy and CodePipeline.
    """
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Hello, World! Deployment successful!",
            "input": event
        })
    }
