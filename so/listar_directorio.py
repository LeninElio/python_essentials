import os

ruta = os.getcwd()

directorio = os.listdir(path=ruta)

for f in directorio:
    print(f)