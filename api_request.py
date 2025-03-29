import boto3
import json
import requests
#from requests_auth_aws_sigv4 import AWSSigV4

# For parsing documents like PDF, use Docling library, then use it through prompt.
# If using IAM role, attach AmazonAPIGatewayInvokeFullAccess policy.
# If API is set OPEN, use WAF to only allow specific IP.

#---- You may skip this part if your API is set OPEN-------------------------------
#session = boto3.Session(
#     aws_access_key_id='',
#     aws_secret_access_key='',
#     region_name='ap-northeast-1'
#    )
#credentials = session.get_credentials()
#auth = AWSSigV4("execute-api", credentials=credentials, region=session.region_name)
#-----------------------------------------------------------------------------------

api_gateway_url = "https://<your-API-here>/default/lambda-create-ppt"

payload = {
    "prompt": "データサイエンスについて",
    }

headers = {"Content-Type": "application/json"}
response = requests.post(api_gateway_url, json=payload, headers=headers, )  #auth=auth,)

print(response.text)
