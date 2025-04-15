import requests

webhook_url = '' # EventStream URL
auth_token = ''  # Authentication token from Event Stream Token Credential Type

data = {
    'event': 'journey_logged_in',
    'message': 'Just a small-town dev, loggin’ in to a big-time system.',
    'user': {
        'user_id': 1981,
        'first_name': 'Steve',
        'last_name': 'Perrynix',
        'email': 'steve.perrynix@journey.linux'
    },
    'terminal': 'tty7',
    'login_method': 'ssh',
    'location': 'South Detroit',
    'auth_status': 'faithfully_authenticated',
    'midnight_train': {
        'destination': 'anywhere',
        'departure_time': '00:00',
        'dnf_payload': 'install_dreams'
    }
}

headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {auth_token}'  # Authorization header
}

response = requests.post(webhook_url, json=data, headers=headers, verify=False) # ssl_verify false

print(f"Status Code: {response.status_code}")
print(f"Response: {response.text}")
