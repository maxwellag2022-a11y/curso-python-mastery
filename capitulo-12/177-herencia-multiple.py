class Volador:

    def volar(self):
        print("Volando")

    def caminar(self):
        print("Camina con dos patas")

class Nadador:

    def nadar(self):
        print("Nadando")

    def caminar(self):
        print("Camina con cuatro patas")

class Pato(Volador,Nadador):
    pass

p = Pato()

p.volar()
p.nadar()
p.caminar()

print(Pato.__mro__)