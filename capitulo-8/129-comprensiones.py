cuadrados = [n ** 2 for n in range(10)]
pares = [n for n in range(20) if n % 2 == 0]

inverso = {v:k for k,v in {"a":1,"b":2}.items()}

unicos = {letra for letra in "fibonacci"}

suma = sum((n for n in range(101)))

print(cuadrados)
print(pares)
print(inverso)
print(unicos)
print(suma)