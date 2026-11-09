# pedir dos numeros
# +,-,*,/,
#realizar la operacion
9
numero_1 = float(input("Ingrese su primero digito: "))
numero_2 = float(input("Ingrese su segundo digito: "))
operador = input("Ingrese su operador: ").strip()

if operador == "+":
    print(f" el resultado de su operacion es: {numero_1 + numero_2}")

elif operador == "-":
    print(f" el resultado de su operacion es: {numero_1 - numero_2}")

elif operador == "*":
    print(f" el resultado de su operacion es: {numero_1 * numero_2}")

elif operador == "/":
    print(f" el resultado de su operacion es: {numero_1 / numero_2}")

else:
    print("Operacion invalida")