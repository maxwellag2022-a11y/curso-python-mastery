class Cuenta_Bancaria:
    pass

    def __init__(self, cuenta, titular,saldo_inicial):
        self.cuenta = cuenta
        self.titular = titular
        self.saldo = saldo_inicial

    def usar_pin(self):
        pin = "4826"
        pin_ingresado = (input("ingrese su pin: "))
        if pin == pin_ingresado:
            return f"tiene acceso a la cuenta \nSu cuenta es {self.cuenta}\nEl titular de esta cuenta es: {self.titular} \nSu Saldo es: {self.saldo}"

        else:
            return f"no tiene acceso a la cuenta {self.cuenta}"
    def login(self):
        inicio = (input("Login - Logout: "))
        if inicio == "login":
            return "Puede continuar"
        else:
            return "Saliendo de Cuenta"

    if login == "Login":
        usar_pin()

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
        print(f"{self.titular}, su cuenta tiene: \nSaldo Q{self.saldo:,.2f}")

    def consultar_historial(self):
        print(f"Su historial es {self.cuenta}")

cuenta1 = Cuenta_Bancaria("Cuenta-56","Flavia",5000)
print(cuenta1.login())
print(cuenta1.usar_pin())
cuenta1.depositar(500)
cuenta1.consultar()
cuenta1.retirar(500)
print(cuenta1.login())