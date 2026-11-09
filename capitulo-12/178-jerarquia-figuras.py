'''
Clase base Figura con metodo abstracto.
Subclass Circulo, Rectangulo y Triangulo que van a
implementar area

mostrar nombre junto al area y usarlo con diccionarios
'''

class Figura:

    def __init__(self, nombre):
        self.nombre = nombre

    def area(self):
        raise NotImplementedError

    def __str__(self):
        return f"Area: {self.area()}"

class Rectangulo(Figura):
    def __init__(self, nombre, altura, base):
        super().__init__(nombre)
        self.altura = altura
        self.base = base

    def area(self):
        return self.base * self.altura


class Triangulo(Figura):
    def __init__(self, nombre, altura, base):
        super().__init__(nombre)
        self.altura = altura
        self.base = base

    def area(self):
        return (self.base * self.altura)/2

class Circulo(Figura):
    def __init__(self, nombre, radio):
        super().__init__(nombre)
        self.radio = radio

    def area(self):
        return 3.1416 * self.radio**2

figuras = [
    Rectangulo('Rectangulo', 3, 6),
    Triangulo('Triangulo', 4, 7),
    Circulo('Circulo', 5)
]

for figura in figuras:
    print(figura)









