'''
Flask application : Client

'''

import requests
import json

url = 'http://127.0.0.1:5000/post'

data = {
    "key": "value"
}

response = requests.post(url, json=data)

print('Response status code:', response.status_code)
print('Response JSON:', response.json())
