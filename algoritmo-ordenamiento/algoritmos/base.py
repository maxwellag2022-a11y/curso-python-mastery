class Ordenamiento:

    def __init__(self, nombre, costo):
        self.nombre = nombre
        self.comparaciones = 0
        self.costo = costo

    def ordenar(self, lista):
        self.comparaciones = 0
        a = lista[:]
        return self._ordenar(a)

    def _ordenar(self, lista):
        raise NotImplementedError("Cada algoritmo debe escribir su _ordenar()")

    def es_mayor(self, x,y):
        self.comparaciones += 1
        return x > y
    def intercambiar(self, a, i, j):
        aux = a[i]
        a[i] = a[j]
        a[j] = aux



