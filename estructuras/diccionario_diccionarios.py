notas = {
    "Calculo": {"pp": 3.5,
                "sp": 2.5,
                "tp": 1.5},
    "Quimica": {"pp": 2.5,
                "sp": 3.0,
                "tp": 5.0},
    "Deporte": {"pp": 2.4,
                "sp": 2.0,
                "tp": 2.2},
    "Logica": {"pp": 1.5,
               "sp": 4.0,
               "tp": 4.5}
}


# Calcular la nota final de cada materia 30, 30, 40
def c31_final():
    global notas
    suma = 0
    for c, v in notas.items():
        n1 = v['pp'] * 0.3
        n2 = v['sp'] * 0.3
        n3 = v['tp'] * 0.4
        suma = n1 + n2 + n3
        v['pr'] = round(suma, 2)
        print(f'La nota final del curso {c}: {round(suma, 2)}')


# calcular el promedio de las notas del estudiante
def c32_final():
    global notas
    promedio = 0

    for v in notas.values():
        promedio += v['pr']
    print(promedio/len(notas))


# mostrar resultados
print('-'*10, 'Notas por materia', '-'*10)
c31_final()
print()
print('-'*7, 'Nota final de estudiante', '-'*7)
c32_final()

