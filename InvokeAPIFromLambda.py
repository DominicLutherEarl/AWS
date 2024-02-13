import json
import urllib3
import boto3
#from aws_requests_auth.aws_auth import AWSRequestsAuth

def lambda_handler(event, context):
    api_url = "https://www.google.com"
    heads = {}
    heads["Authorization"] = "Bearer testCred"
    http = urllib3.PoolManager()
  
    response = http.request('GET', api_url, timeout=10, headers=heads)
    
    return {
        'statusCode': 200,
        'body': json.dumps(response.status)
    }
