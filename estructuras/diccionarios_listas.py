notas = {
    'Calculo': [3.5, 2.5, 1.5], 
    'Quimica': [2.5, 3.0, 5.0], 
    'Deporte': [2.4, 2.0, 2.2], 
    'Logica': [1.5, 4.0, 4.5]
}


# Calcular la nota final de cada materia
def c21_final():
    global notas
    suma = 0
    for c, v in notas.items():
        n1 = v[0] * 0.3
        n2 = v[1] * 0.3
        n3 = v[2] * 0.4
        suma = n1 + n2 + n3
        v.append(round(suma, 2))
        print(f'La nota final de {c} es {round(suma, 2)}')


# calcular el promedio de las notas del estudiante
def c22_final():
    global notas
    promedio = 0
    for v in notas.values():
        promedio += v[-1]/len(v)
    print(promedio)

# mostrar resultados
print('-'*10, 'Notas por materia', '-'*10)
c21_final()
print()
print('-'*7, 'Nota final de estudiante', '-'*7)
c22_final()


