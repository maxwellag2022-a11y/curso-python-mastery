def estadistica(numeros):
    return min(numeros), max(numeros), sum(numeros)/len(numeros)

minimo,maximo,promedio = estadistica([5,9,3,7,1,8])
print(f"Min: {minimo}, Max: {maximo}, Promedio: {promedio}")