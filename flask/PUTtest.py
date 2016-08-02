import requests
import datetime

value = 669
quality = 192
timestamp = str(datetime.datetime.now())

data = {
    "value":value,
    "quality":quality,
    "timestamp":timestamp
}

r = requests.put('http://192.168.110.5:5000/dados.taginterno1',json=data)

print r.json()
