import os

nueva_carpeta = input('Nombre de la carpeta: ')

dir_actual = os.getcwd()
path = os.path.join(dir_actual, nueva_carpeta)

# primer metododo de comprobacion de exixtencia
if os.path.exists(path):
    print(f'La carpeta {nueva_carpeta} ya existe')
else:
    os.makedirs(path)
    print(f'La carpeta {nueva_carpeta} fue creada')

# otro metodo para comprobar la existencia
try:
    os.makedirs(path)
except FileExistsError:
    print(f'La carpeta {nueva_carpeta} ya existe')