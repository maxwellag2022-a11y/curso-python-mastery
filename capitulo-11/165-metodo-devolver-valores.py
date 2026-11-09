class Rectangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)

    def es_cuadrado(self):
        return self.base == self.altura

rectangulo1 = Rectangulo(5,2)
print(f"Area: {rectangulo1.area()}\nPerimetro: {rectangulo1.perimetro()}\nEs cuadrado: {rectangulo1.es_cuadrado()}")

rectangulo2 = Rectangulo(5, 5)
print("Es cuadrado: ", rectangulo2.es_cuadrado())