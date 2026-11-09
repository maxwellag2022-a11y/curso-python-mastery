factorial = int(input("Ingrese el numero que desee calcular el factorial: "))

resultado = 1 #variable acumuladora, hay que saber inicializar
for numero in range(1, factorial + 1):
    resultado = resultado * numero

print(f"El factorial de {factorial} es: {resultado}")