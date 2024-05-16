import requests
import time

url = 'http://127.0.0.1:5000/get'


while True:
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print('Received data:', data)
    else:
        print('Failed to retrieve data. Status code:', response.status_code)
    time.sleep(1)