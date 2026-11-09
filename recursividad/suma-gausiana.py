def suma_gauss(n):

    if n == 1:
        return 1

    resultado = n + suma_gauss(n - 1)
    return resultado

print("resultado = ", suma_gauss(50))


# costo 0(n²)