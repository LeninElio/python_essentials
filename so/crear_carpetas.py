import os

nueva_carpeta = input('Nombre de la carpeta: ')

dir_actual = os.getcwd()

path = os.path.join(dir_actual, nueva_carpeta)

os.makedirs(path)