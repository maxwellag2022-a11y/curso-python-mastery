import time

def cronometrar(func, *args, **kwargs):
    '''
        ejecutar funcion con sus argumentos
         y mide cuanto tiempo tarda
    '''

    inico = time.time() #captura la hora 3:48
    resultado = func(*args, **kwargs)
    duracion = time.time() - inico
    print(f"{func.__name__} tardo {duracion:.4f} segundos")
    return resultado

def sumar_hasta(n):
    total = 0
    for i in range(n):
        total += i

    return total

resultado = cronometrar(sumar_hasta, 1000000)
print(resultado)