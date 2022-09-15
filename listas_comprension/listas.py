import random

lista = []

for i in range(10):
    lista.append(i)
print(lista)

comp = [j/2 for j in range(10) if j%2!=0]
print(comp)

nombre = ['Juan', 'Pedro', 'Pablo', 'Eder']
nombre = [i[::-1] for i in nombre]
print(nombre)


class Estudiante:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota


estudiantes = list()
for i in nombre:
    nota = random.randint(1, 20)
    e = Estudiante(i, nota)
    estudiantes.append(e)

for obj in estudiantes:
    print(obj.nombre, obj.nota, end='\n')