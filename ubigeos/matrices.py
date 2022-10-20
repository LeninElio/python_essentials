datos = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# print(datos)

# for dato in range(len(datos)):
#     # print(datos[dato])
#     for dat in range(len(datos[dato])):
#         print(datos[dato][dat], end=" ")
#     print()


# comprimir = [i for dato in datos for i in dato]

# print(comprimir)

num = int(input("Enter the number of rows: "))

for i in range(0, num):
    for j in range(0, num-i-1):
        print(end=" ")
    for j in range(0, i+1):
        print("*", end=" ")
    print()
