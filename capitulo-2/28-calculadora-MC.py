print("=== CALCULADORA IMC ===")
nombre = input("Ingrese su nombre: ").strip().title()
peso = float(input("Ingrese su peso en Kg.: "))
altura = float(input("ingrese su altura en metros.: "))

imc = peso / (altura ** 2)
print(f"\nHola {nombre}")
print(f"Tu IMC es: {imc:.2f}")