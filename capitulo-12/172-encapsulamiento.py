class Cuenta:

    def __init__(self, titular, saldo):
        self.titular = titular
        self._historial = []
        self.__saldo = saldo

    def depositar(self, monto):
        self.__saldo += monto
        self._historial.append(("dep", monto))

    def obtener_saldo(self):
        return self.__saldo

cuenta1 = Cuenta("Fede", 1000)

print(cuenta1.titular)
print(cuenta1._historial)
#print(cuenta1.__saldo)
print(cuenta1.depositar(1000))
print(cuenta1.obtener_saldo())
