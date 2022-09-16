from urllib.request import urlopen
import json

url = " https://random-data-api.com/api/commerce/random_commerce?size=100"
response = urlopen(url)

data = json.loads(response.read())

# print(type(data[1]))

for i in data:
    # siemptre uso clave, valor para no olvidarme de la formacion de un diccionario
    for clave, valor in i.items():
        print(f'Dato: {clave}: {valor}')
    break