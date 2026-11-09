matriz = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
]

print(matriz)
print(f"{matriz[0]}\n{matriz[1]}\n{matriz[2]}")
print(f"{matriz[0]}")
print(f"{matriz[1]}")
print(f"{matriz[2]}")
print()
print(matriz[1][1])
print()
for fila in matriz:
    for valor in fila:
        print(valor, end=" ")
    print()