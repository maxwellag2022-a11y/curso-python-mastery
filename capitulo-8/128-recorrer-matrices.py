matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for fila in matriz:
    for valor in fila:
        print(valor, end=" ")
    print()

for i, fila in enumerate(matriz):
    for j, valor in enumerate(fila):
        print(f"M[{i}][{j}] = {valor}")