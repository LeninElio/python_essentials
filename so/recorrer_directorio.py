import os

ruta = os.getcwd()

with os.scandir(path=ruta) as listado:
    for i in listado:
        if i.is_dir():
            print(f'Es una carpeta -> {i.name}')
        elif i.is_file():
            print(f'Es un archivo -> {i.name}')