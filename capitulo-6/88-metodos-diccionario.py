notas = {"Luis":85, "Maria":92, "Pedro":78}

print(notas.keys())
print(notas.values())
print(notas.items())

print(list(notas.keys()))
print(list(notas.items()))

inventario = {}
inventario.setdefault("Manzanas",0)
print(inventario)
inventario["Manzanas"] += 5
print(inventario)