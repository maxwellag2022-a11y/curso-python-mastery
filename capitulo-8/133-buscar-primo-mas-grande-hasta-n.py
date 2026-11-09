n = int(input("Ingrese su numero: "))
mayor_primo = None

for candidato in range(n,1,-1):
    es_primo = True
    for divisor in range(2, int(candidato ** 0.5) + 1):
        if candidato % divisor == 0:
            es_primo = False
            break

    if es_primo:
        mayor_primo = candidato
        break

if mayor_primo:
    print(f"El numero primo mas grande, menor o igual a {n}, es {mayor_primo}")
else:
    print(f"No hay primos menores a {n}")