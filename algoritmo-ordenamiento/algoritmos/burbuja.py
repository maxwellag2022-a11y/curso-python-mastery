from algoritmos.base import Ordenamiento

class Burbuja(Ordenamiento):

    def __init__(self):
        super().__init__("Burbuja", "O(n²)")

    def _ordenar(self, a):

        n = len(a)
        for i in range(1, n):
            for j in range(0, n - i):

                if self.es_mayor(a[j], a[j + 1]):
                    self.intercambiar(a, j, j + 1)


        return a
