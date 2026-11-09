nombres = ["Fede", "Daniel", "Marcos"]
notas = [85, 92, 78]

print(list(zip(nombres, notas)))

for nombre, nota in zip(nombres, notas):
    print(f"{nombre} - {nota}")