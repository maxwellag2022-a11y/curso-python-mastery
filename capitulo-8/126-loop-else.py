nombres = ["Federico", "Daniel", "Marcos", "Marilu", "Aldara", ]
buscado = "Pedro"

for nombre in nombres:
    if nombre == buscado:
        print("Encontrado ✅ ")
        break

else:
    print(f"{buscado} no se encuentra en la lista ❌")