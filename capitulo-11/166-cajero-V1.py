'''
Clase: Cuenta, titular, pin, historial de transacciones
metodos: depositar, retirar, consultar_Saldo, ver_historial
solo una cuenta
menu: login -> logout
while_True

salir: break or continue
pin while true
while true

login
registrar

'''

class Cuenta_Bancaria:
    pass

    def __init__(self, cuenta, titular, Pin, saldo,  historial_de_transaccion):
        self.cuenta = cuenta
        self.titular = titular
        self.Pin = Pin
        self.saldo = saldo
        self.historial_de_transaccion = historial_de_transaccion
        self.acceso_permitido = f"str(cuenta) \nstr(titular) \nstr(saldo) \nstr(historial_de_transaccion)"

    def usar_pin(self):
        Pin = 4826
        pin_ingresado = (int(input("ingrese su pin: ")))
        if pin_ingresado == self.Pin:
            return f"Tiene ingreso a la cuenta {self.cuenta}\n {self.acceso_permitido}"
        else:
            return f"No tiene ingreso a la cuenta {self.cuenta}"

    def depositar(self, monto):
        if monto <= 0:
            print("Monto Invalido")
            return
        self.saldo += monto
        print(f"+ Q{monto:,.2f} Depositados. \nSaldo Q{self.saldo:,.2f}")

    def retirar(self, monto):
        if monto > self.saldo:
            print("Saldo insuficiente")
            return
        self.saldo -= monto
        print(f"+ Q{monto:,.2f} retirados. \nSaldo Q{self.saldo:,.2f}")

    def consultar(self):
        print(f"{self.titular}. \nSaldo Q{self.saldo:,.2f}")






cuenta1 = Cuenta_Bancaria()