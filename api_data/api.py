from urllib.request import urlopen
import json

url = " https://random-data-api.com/api/commerce/random_commerce?size=100"
response = urlopen(url)

data = json.loads(response.read())

for datos in data:
    print(datos['id'])