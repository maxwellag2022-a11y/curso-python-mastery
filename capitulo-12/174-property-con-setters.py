class Temperatura:

    def __init__(self,celcius = 0):
        self._celcius = celcius

    @property
    def celcius(self):
        return self._celcius

    @celcius.setter
    def celcius(self,valor):
        if valor < -273.15:
            raise ValueError ("No existen temperaturas bajo el cero absoluto")

        self._celcius = valor

    @property
    def farenheit(self):
        return self._celcius * 1.8 + 32

temp1 = Temperatura(25)
print(temp1.celcius)
print(temp1.farenheit)
temp1.celcius = 100
print(temp1.celcius)
print(temp1.farenheit)
temp1.celcius = -300