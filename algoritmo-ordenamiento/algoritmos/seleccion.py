from algoritmos.base import Ordenamiento

class Seleccion(Ordenamiento):
    def __init__(self):
        super().__init__("Seleccion","O(n²)")

    def _ordenar(self, a):
        n = len(a)
        for i in range(0, n - 1):
            pos_menor = i
            for j in range(i + 1, n):
                if self.es_mayor(a[pos_menor], a[j]):
                    pos_menor = j
            self.intercambiar(a, i, pos_menor)
        return a
