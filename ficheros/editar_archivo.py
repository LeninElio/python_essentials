with open('ficheros/file.txt', mode='a', encoding='utf-8') as ar:
    for i in range(1, 10):
        ar.write(f'{i}\n')
        
ar.close()
