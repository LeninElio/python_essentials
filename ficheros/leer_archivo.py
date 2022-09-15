with open('ficheros/output.txt', mode='r', encoding='utf-8') as ar:
    archivo = ar.readlines()


for linea in archivo:
    print(linea, end='')


ar.close()