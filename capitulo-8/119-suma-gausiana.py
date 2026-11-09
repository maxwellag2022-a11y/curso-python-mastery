digito =  int(input("Digite el numero que desee sumar:"))

inicio = 0
for numero in range(1, digito + 1):
    inicio = inicio + numero

print(f"La suma gausiana de {digito} es: {inicio}")