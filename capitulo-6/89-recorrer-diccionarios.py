notas = {"Luis":85, "Maria":92, "Pedro":78}

for nombre in notas:
    print(nombre)

for nombre in notas.keys():
    print(nombre)

print()
for nombre in notas.values():
    print(nombre)

print()

for nombre,nota in notas.items():
    print(f"{nombre} - {nota}")

print(f"Promedio: {sum(notas.values()) / len(notas)}")

