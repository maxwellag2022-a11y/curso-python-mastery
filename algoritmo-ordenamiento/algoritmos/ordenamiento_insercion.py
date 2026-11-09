from algoritmos.base import Ordenamiento

class Insercion(Ordenamiento):
    def __init__(self):
        super().__init__("Insercion", "O(n²)")

    def _ordenar(self, a):
        for i in range(1, len(a)):
            actual = a[i]
            j = i - 1
            while j >= 0 and self.es_mayor(a[j], actual):
                a[j + 1] = a[j]
                j -= 1
            a[j + 1] = actual
        return a

