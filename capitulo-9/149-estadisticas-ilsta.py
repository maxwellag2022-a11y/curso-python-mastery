def estadiscitas(numeros):
    if not numeros:
        return None
    return {
        "min": min(numeros),
        "max": max(numeros),
        "Promedio": sum(numeros)/ len(numeros),
        "rango": max(numeros) - min(numeros)
    }



datos = [85, 72, 98, 65, 88, 95, 78]
stats = estadiscitas(datos)

for clave, valor in stats.items():
    print(f"{clave}: {valor}")

