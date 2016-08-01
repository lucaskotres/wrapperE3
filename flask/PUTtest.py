import requests
import datetime

value = 669
quality = 192
timestamp = str(datetime.datetime.now())
print timestamp

r = requests.put('http://192.168.110.5:5000/dados.taginterno1',json={"value":value,"quality":quality,"timestamp":timestamp})

print r.json()
