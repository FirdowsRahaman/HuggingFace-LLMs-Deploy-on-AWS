import requests
import json

# AWS REST URL
aws_rest_url = "your REST API url"

# Payload
payload = json.dumps({"inputs": "some inputs"})

# Send request
result = requests.post(aws_rest_url, data=payload, headers={"content-type": "application/json", "x-api-key": ""})

print(result.text)
