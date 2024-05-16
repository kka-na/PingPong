'''
Flask application : Client

'''

import requests
import json

url = 'http://Mobina.access.ly:5000/post'

file_path = './taxi.json'

with open(file_path, 'r') as file:
    data = json.load(file)

response = requests.post(url, json=data)

print('Response status code:', response.status_code)
print('Response JSON:', response.json())
