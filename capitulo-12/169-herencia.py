class Empleado:

    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def presentarse(self):
        print(f"Soy {self.nombre}")

    def calcular_sueldo(self):
        return self.salario * 1.20

class Programador(Empleado):

    def __init__(self, nombre, salario, lenguaje):
        super().__init__(nombre, salario)
        self.lenguaje = lenguaje

    def codear(self):
        print(f"{self.nombre} esta codeando en {self.lenguaje}")

class Gerente(Empleado):

    def __init__(self, nombre, salario, equipo):
        super().__init__(nombre, salario)
        self.equipo = equipo

    def asignar_tarea(self, persona, tarea):
        print(f"{self.nombre} asignó  '{tarea}' a {persona}")

fede = Programador("Fede", 9500, "Python")
fede.presentarse()
fede.codear()
print(fede.calcular_sueldo())

equipo = ["Marcos","Marilu"]
daniel = Gerente("Daniel", 9500,equipo)
daniel.presentarse()
daniel.asignar_tarea(equipo[1],"Setup de servidor")