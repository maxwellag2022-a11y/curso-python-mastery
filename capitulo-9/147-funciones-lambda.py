cuadtrado = lambda x: x**2
print(cuadtrado(5))
print(cuadtrado(7))

suma = lambda a, b: a + b
print(suma(5, 7))

nombres = ["Maria","Luis","Ana", "Pedro"]
entrada = sorted(nombres, key=lambda x: len(x))
print(entrada)

precios = [100,250,480,320]
con_iva = list(map(lambda p: round(p * 1.12,2), precios))

print(con_iva)

caros = list(filter(lambda p: p > 200, precios))
print(caros)