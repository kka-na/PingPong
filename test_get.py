import requests
import time

url = 'http://Mobinha.access.ly:5000/get'

id_list = ['kana']

while True:
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        for key,value in data.items():
            if key in id_list:
                if value['state'] == 'call':
                    call_position = [value['position']['latitude'],value['position']['longitude'] ]
                    print(f"{key} called! at position lat:{call_position[0]} lng:{call_position[1]}")
        print('Received data:', data)
    else:
        print('Failed to retrieve data. Status code:', response.status_code)
    time.sleep(1)