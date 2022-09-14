notas = [
    {"nombre": "calculo",
     "pp": 3.5,
     "sp": 2.5,
     "tp": 1.5},
    {"nombre": "Quimica",
        "pp": 2.5,
        "sp": 3.0,
        "tp": 5.0},
    {"nombre": "Deporte",
        "pp": 2.4,
        "sp": 2.0,
        "tp": 2.2},
    {"nombre": "Logica",
        "pp": 1.5,
        "sp": 4.0,
        "tp": 4.5}
]


# Calcular la nota final de cada materia 30, 30, 40
def c41_final():
    global notas
    suma = 0

    for i in notas:
        n1 = i['pp'] * 0.3
        n2 = i['sp'] * 0.3
        n3 = i['tp'] * 0.4
        suma = n1 + n2 + n3

        i['nf'] = round(suma, 2)

        print(f'Nota final del curso {i["nombre"]}: {round(suma, 2)}')


# calcular el promedio de las notas del estudiante
def c42_final():
    global notas
    promedio = 0

    for i in notas:
        promedio += i['nf']

    print(f'Promedio del Estudiante: {promedio/len(notas)}')


# mostrar resultados
print('-'*10, 'Notas por materia', '-'*10)
c41_final()
print()
print('-'*7, 'Nota final de estudiante', '-'*7)
c42_final()
