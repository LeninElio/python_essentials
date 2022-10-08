# Analizar datos

# 1. Cuantos sobrevivieron ?
# 2. Porcentaje de las personas que sobrevivieron
# 3. Cuantas clases hay ?
# 4. Cuantos hombres y cuantas mujeres hubo
# 5. Cuantos ticket diferentes habia ?

import csv

titanic = []
dic = {}

vivos = 0
muertos = 0

with open('data/titanic.csv') as archivo:
    datos = csv.reader(archivo, delimiter='\t')
    for linea in datos:
        print(linea)
        titanic.append(linea)


titulos = titanic[0]
del(titanic[0])

for pasajero in titanic:
    if pasajero[1] == '1':
        vivos += 1
    elif pasajero[1] == '0':
        muertos += 1

# 1. Cuantos sobrevivieron ?
print('*'*50)
pasajeros = vivos + muertos
print(f'El titanic transportaba {pasajeros} pasajeros')
print()
print(f'N° de sobrevivientes: {vivos}, N° de desesos: {muertos}')
print()
# 2. Porcentaje de las personas que sobrevivieron
print('*'*50)
porcentaje = (vivos * 100)/pasajeros
print(f'El porcentaje de sobrevivientes es: {round(porcentaje, 2)} %')
print()

clases = []
for clase in titanic:
    clases.append(clase[2])

clases = set(clases)
# clases = list(clases)

# 3. Cuantas clases hay ?
print('*'*50)
print(f'Dentro del titanic habia {len(clases)} clases')
print()

masculino, femenino = 0, 0
for sexo in titanic:
    if sexo[4] == 'male':
        masculino += 1
    elif sexo[4] == 'female':
        femenino += 1
# 4. Cuantos hombres y cuantas mujeres hubo

print('Dentro del titanic habia: ')
print(f'• {masculino} Hombres')
print(f'• {femenino} Mujeres')
print()


tickets = []
for ticket in titanic:
    tickets.append(ticket[8])

tickets = set(tickets)

# 5. Cuantos ticket diferentes habia ?
print('*'*50)
print(f'En el titanic hubo {len(tickets)} diferentes tickets')