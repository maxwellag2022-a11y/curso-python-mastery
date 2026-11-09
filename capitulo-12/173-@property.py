class Rectangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    @property
    def area(self):
        return self.base * self.altura

    @property
    def perimetro(self):
        return 2 * (self.altura + self.base)

rectangulo1 = Rectangulo(5,3)
print(rectangulo1.area)