notas = [
    ['Calculo', 3.5, 2.5, 1.5], 
    ['Quimica', 2.5, 3.0, 5.0], 
    ['Deporte', 2.4, 2.0, 2.2], 
    ['Logica', 1.5, 4.0, 4.5]
    ]

# calcula la nota final de cada materia (30%, 30%, 40%)
def c11_final():
    global notas
    for i in range(len(notas)):
        m1 = notas[i][1] * 0.3
        m2 = notas[i][2] * 0.3
        m3 = notas[i][3] * 0.4
        promedio = m1 + m2 + m3
        notas[i].append(round(promedio, 2))
        print(f'El promedio de {notas[i][0]}: {round(promedio, 2)}')


# Calcule el promedio de las notas del estudiante
def c12_promedio():
    global notas
    promedio_final = 0
    for i in notas:
        promedio_final += i[-1]
    print(f'Promedio general del estudiante es: {promedio_final/len(notas)}')



# llamamos las funciones y mostramos los resultados
print('-'*10, 'Primer resultado', '-'*10)
c11_final()
print()
print('-'*10, 'Segundo resultado', '-'*10)
c12_promedio()