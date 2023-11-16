import requests
import json

url = "http://127.0.0.1:5000/predict"  # Change this to the actual URL of your Flask API endpoint

event = {
    # "body": "{\"inputs\": {\"question\": \"What are we having for dinner?\",\"context\": \"I'm at a restaurant, pizza, turkey.\"}}",
    
    "headers": {
        "Content-Type": "application/json"
    },
    "requestContext": {
       
        "requestTimeEpoch": 1646419766417,
        "requestId": "request-id",
        "identity": {
            "cognitoIdentityPoolId": None,
            "accountId": None,
         
            "userArn": None,
            "userAgent": "test-invoke-user-agent",
            "user": None
        },
        "domainName": "test-invoke-api-id.execute-api.your-region.amazonaws.com",
        "apiId": "your-api-id"
    },
    "body": "{\"inputs\": {\"question\": \"Where are the drinks?\",\"context\": \"I'm the pub.\"}}",
    "isBase64Encoded": False
}

headers = {
    "Content-Type": "application/json"
}

# Send the POST request
response = requests.post(url, data=json.dumps(event), headers=headers)

# Print the response
print("Response Code:", response.status_code)
print("Response Body:", response.json())
