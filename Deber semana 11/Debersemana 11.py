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


