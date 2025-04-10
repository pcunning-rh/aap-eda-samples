import requests

webhook_url = '' # EventStream URL
auth_token = ''  # Authentication token from Event Stream Token Credential Type


data = {
    'event': 'user_created',
    'message': 'Sample message content from service',
    'user': {
        'user_id': 12345,
        'first_name': 'John',
        'last_name': 'Doe',
        'email': 'john.doe@example.com'
    }
}
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {auth_token}'  # Authorization header
}

response = requests.post(webhook_url, json=data, headers=headers, verify=False) # ssl_verify false

print(f"Status Code: {response.status_code}")
print(f"Response: {response.text}")
