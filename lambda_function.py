import os
import json
import boto3

print(boto3.__version__)
ENDPOINT_NAME = os.environ['ENDPOINT_NAME']
runtime = boto3.client('runtime.sagemaker')


def lambda_handler(event, context):

    payload = json.dumps(event)
    print("Received event: " + payload)

    response = runtime.invoke_endpoint(
        EndpointName=ENDPOINT_NAME,
        ContentType='application/json',
        Body=bytes(payload, 'utf-8')
    )
    print(response)

    result = json.loads(response['Body'].read().decode())
    print(result)

    return result
     