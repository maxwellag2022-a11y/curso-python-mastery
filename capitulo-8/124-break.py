nombres = ["Federico", "Daniel", "Marcos", "Marilu", "Aldara", ]
buscado = "Daniel"

for nombre in nombres:
    if buscado == nombre:
        print(f"Encontrado {nombre}")
        break
    print(f"buscando {nombre}")