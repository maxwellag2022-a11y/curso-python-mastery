llamadas = 0
def potencia_rapida(a,n,mostrar=False):

    global llamadas
    llamadas += 1

    if n == 0:
        return 1

    mitad = potencia_rapida(a,n//2,mostrar)

    if n%2 == 0:
        return mitad * mitad
    else:

        return a * mitad * mitad

print(potencia_rapida(2,10),llamadas)