# HuggingFace-LLMs-Deploy-on-AWS

### Overview
This guide demonstrates how to deploy HuggingFace Large Language Models (LLMs) as REST APIs using AWS SageMaker and AWS Lambda. 
By following these steps, you can easily create a scalable and serverless architecture to deploy and utilize LLMs for various natural language processing tasks.

### Step 1: Deploy LLM Model on AWS SageMaker
1. Go to the Amazon SageMaker Console.
2. Navigate to the Inference section and click on Endpoints.
3. Check if the model endpoint has been created and is currently in service.

### Step 2: Create AWS Lambda Function
1. Go to AWS Lambda to create a serverless lambda function.
2. Click on "Create function".
   - Function Name: HuggingFaceLLMDeploy
   - Runtime: Python3.10
3. Click "Create Function".
4. Write the Python code in the `lambda_function.py` file.
5. Click on "Deploy".
6. Go to the Configuration tab.
  - Click on Environment variables.
  - Click on Edit.
  - Click on Add environment variable.
    - Key: ENDPOINT_NAME
    - Value: SageMaker model endpoint name
  - Click on Save.
7. Go to General configuration.
  - Edit the Timeout to 3 min.
8. Go to the Test tab.
  - Write Event name: test_lambda
  Event JSON:
``{
  "inputs": "write about blockchain"
}``
