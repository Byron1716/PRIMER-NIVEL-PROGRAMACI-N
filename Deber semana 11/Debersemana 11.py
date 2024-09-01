arr_bid=[
    [3, 6, 7],
    [2, 8, 9],
    [10, 13, 17]
]
v =int(input("¿Qué valor deseas buscar?: "))
fila = -1
columna = -1
for i in range(len(arr_bid)):
    for j in range(len(arr_bid)):
        if arr_bid[i][j] == v:
            fila = i
            columna = j
            break
    if fila != -1:
        break

print("")
if fila != -1:
    print(f"Se encontró el número {v} en la fila {fila} y columna {columna}")
else:
    print(f"El número {v} no se encontró")


#Parte 2 del Deber
#Ordenar una matriz de forma ascendente
A=[
    [4, 9, 25, 21],
    [2, 134, 12, 85],
    [99, 123, 19, 22],
    [78, 32, 76, 44]
]
print("")
print("Esta es la lista sin ordenar")
print(A)

print("")

v = A[0]
v.sort()
b = A[1]
b.sort()
n = A[2]
n.sort()
m = A[3]
m.sort()
print("")
print("Esta es la lista ya ordenada")
print("[",v,",",b,",",n,",",m,"]")