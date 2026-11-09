from datetime import datetime

class Cuenta:
    '''
    Representa una cuenta bancaria
    con operaciones basicas
    '''

    contador_id = 0

    def __init__(self, titular, pin, saldo,):
        Cuenta.contador_id += 1
        self.id_cuenta = Cuenta.contador_id
        self.titular = titular
        self.pin = pin
        self.saldo = saldo
        self.historial = []
        self.registrar("Apertura", self.saldo)

    def registrar(self, tipo, monto):
        '''
        Metodo interno para guardar una transaccion
        '''

        self.historial.append({
            "fecha": datetime.now().strftime("%Y - %m - %d : %H:%M:%S"),
            "tipo": tipo,
            "monto": monto,
            "saldo_resultante": self.saldo
        })

    def validar_pin(self, pin_intento):
        return pin_intento == self.pin

    def depositar(self, monto):
        if monto <= 0:
            return False, "El monto debe ser positivo"
        self.saldo += monto
        self.registrar("DEPOSITO", monto)
        return True, f"Depositados Q.{monto:,.2f}"

    def retirar(self, monto):
        if monto <= 0:
            return False, "El monto debe ser positivo"
        if monto > self.saldo:
            return False, f"Saldo insuficiente. Tu saldo es Q.{self.saldo:,.2f}"
        self.saldo -= monto
        self.registrar("RETIRO", monto)
        return True, f"Retirados Q.{monto:,.2f}"

    def consultar_saldo(self):
        return self.saldo

    def ver_historial(self, ultimos = 10):
        return self.historial[-ultimos:]

    def __str__(self):
        return f"Cuenta #{self.id_cuenta} - {self.titular} - Q{self.saldo:,.2f}"

#Mi base de datos utilizando diccionarios

cuentas_db = {
    "001": Cuenta("Federico Arriola", "4826", 5000),
    "002": Cuenta("Daniel Esquivel", "6824", 12000),
    "003":Cuenta("Marcos Bolivar", "0000", 250)
}

def login():
    '''
    Funcion oara hacer login
    '''

    print()
    print("="*50)
    print("\t\t\tCAJERO FIBONACCI BANK")
    print("="*50)

    intentos = 3
    while intentos > 0:
        cuenta_id = input("\nNumero de cuenta: ").strip()
        if cuenta_id not in cuentas_db:
            print("Cuenta no encontrada")
            intentos -= 1
            continue
        cuenta = cuentas_db[cuenta_id]
        pin = input("\nPIN :").strip()
        if cuenta.validar_pin(pin):
            print(f"\nBienvenido, {cuenta.titular}")
            return cuenta

        intentos -=1
        print(f"Pin incorrecto, Intentos restantes: {intentos}")

    print("Demasiados intentos fallidos, cuenta bloqueada")
    return None

def menu_cuenta(cuenta):
    while True:
        print("\n=== MENÚ ===")
        print("1) Consultar Saldo")
        print("2) Depositar")
        print("3) Retirar")
        print("4) Ver historial")
        print("0) Salir")

        op = input("Opcion: ").strip()

        if op == "1":
            print(f"\nSaldo Actual: Q.{cuenta.consultar_saldo():,.2f}")

        elif op == "2":
            try:
                monto = float(input("Monto a depositar: Q. "))
                ok, msg = cuenta.depositar(monto)
                print(msg)
            except ValueError:
                print("monto invalido")

        elif op == "3":
            try:
                monto = float(input("Monto a retirar: Q. "))
                ok, msg = cuenta.retirar(monto)
                print(msg)
            except ValueError:
                print("monto invalido")

        elif op == "4":
            print(f"\nHistorial reciente:")
            print(f"{'FECHA':<22}{'TIPO':<12}{'MONTO':>12}{'SALDO':>14}")
            print("-"*60)
            for t in cuenta.ver_historial():
                print(f"{t['fecha']:<22}{t['tipo']:<12}{t['monto']:>11,.2f}Q.{t['saldo_resultante']:>13}")

        elif op == "0":
            print(f"\nGracias por usar Fibonacci Bank, {cuenta.titular}")
            break

        else:
            print("Opcion incorrecta")

if __name__ == "__main__":
    while True:
        cuenta = login()
        if cuenta:
            menu_cuenta(cuenta)

        otro = input("\n Otra operacion?: (s/n) ").strip().lower()
        if otro != "s":
            break

        print("Adios")

