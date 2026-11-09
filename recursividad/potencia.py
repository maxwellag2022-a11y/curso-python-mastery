llamadas = 0

def potencia(a,n):


    global llamadas
    llamadas += 1
    if n == 0:
        return 1

    return a * potencia(a,n-1)

print(potencia(2,300))