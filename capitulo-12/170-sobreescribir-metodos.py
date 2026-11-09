class Empleado:

    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def calcular_sueldo(self):
        return self.salario

class Programador(Empleado):

    def __init__(self, nombre, salario):
        super().__init__(nombre, salario)

    def calcular_sueldo(self):
        return self.salario * 1.10

class Gerente(Empleado):

    def __init__(self, nombre, salario):
        super().__init__(nombre, salario)

    def calcular_sueldo(self):
        return self.salario * 1.25

empleados = [
    Empleado("Marcos", 5000),
    Programador("Federico", 9500),
    Gerente("Daniel", 15000)
]

for e in empleados:
    print(f"{e.nombre}: Q.{e.calcular_sueldo()}")