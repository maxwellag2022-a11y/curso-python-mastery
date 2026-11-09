class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        return "El animal hablando"

class Perro(Animal):

    def hablar(self):
        return "Guau!"

class Gato(Animal):

    def hablar(self):
        return "Miau!"

class Vaca(Animal):

    def hablar(self):
        return "Moo!"

animales = [Perro("Rex"), Gato("Whiskers"), Vaca("Bessie")]

for animal in animales:
    print(animal.hablar())