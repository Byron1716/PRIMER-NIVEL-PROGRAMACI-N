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