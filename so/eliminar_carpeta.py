import os

eliminar = input('Ingrese el nombre de la carpeta a eliminar: ')
ruta = os.getcwd()

path = os.path.join(ruta, eliminar)

if os.path.exists(path):
    os.rmdir(path)
    print(f'La carpeta {eliminar} fue eliminada correctamente')
else:
    print(f'La carpeta {eliminar} no existe')