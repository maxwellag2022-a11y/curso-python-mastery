# 1,1,2,3,5,8,13,21,34,
# phi
lista = []
def suma_fibonacci(n):

    global lista
    if n <= 1:
        return n

    return suma_fibonacci(n-1) + suma_fibonacci(n-2)

lista = [suma_fibonacci(n) for n in range(10)]
print(lista)