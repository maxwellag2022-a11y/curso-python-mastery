class CuentaBancaria:

    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self.saldo = saldo_inicial

    def dipositar(self, monto):
        if monto <= 0:
            print("Monto Invalido")
            return
        self.saldo += monto
        print(f"+ Q{monto:,.2f} Depositados. \nSaldo Q{self.saldo:,.2f}")

    def retirar(self, monto):
        if monto > self.saldo:
            print(f"Saldo insuficiente. Tienes Q{self.saldo:,.2f} ")
            return
        self.saldo -= monto
        print(f"+ Q{monto:,.2f} retirados. \nSaldo Q{self.saldo:,.2f}")

    def consultar(self):
        print(f"{self.titular}. \nSaldo Q{self.saldo:,.2f}")

cuenta = CuentaBancaria("Flavia", 1000)
cuenta.consultar()
cuenta.dipositar(500)
cuenta.retirar(200)
cuenta.retirar(10000)