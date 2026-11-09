class Auto:
    def __init__(self, marca, modelo, anio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.encendido = False

    def encender(self):
        self.encendido = True
        print(f"{self.marca} {self.modelo} encendido")

    def apagar(self):
        self.encendido = False
        print(f"{self.marca} {self.modelo} apagado")


mi_auto_1 = Auto("Toyota", "Corolla", 2020)
mi_auto_2 = Auto("Honda", "Civic", 2018)

print(mi_auto_1.marca)
print(mi_auto_2.anio)

mi_auto_1.encender()
print(mi_auto_1.encendido)

print(mi_auto_2.encendido)

