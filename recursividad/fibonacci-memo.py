def fibonacci(n, memoria = None):
    ''' Version con memoria, guardar los resultados
    ya calculados para no repetirlos. de O(n²)'''

    if memoria is None:
        memoria = {}

    if n <= 1:
        return n

    if n in memoria:
        return memoria[n]

    memoria[n] = fibonacci(n-1, memoria) + fibonacci(n-2, memoria)

    return memoria[n]

print([fibonacci(i) for i in range(50)])

#O(n²)