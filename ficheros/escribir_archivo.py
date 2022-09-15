with open('ficheros/file.txt', mode='w', encoding='utf-8') as ar:
    for i in range(1, 10):
        ar.write(f'{i}\n')
        
ar.close()


with open('ficheros/file.txt', mode='r', encoding='utf-8') as ar:
    for j in ar.readlines():
        print(j, end='')

ar.close()