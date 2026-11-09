
lado_1 = float(input("Ingrese su primero digito: "))
lado_2 = float(input("Ingrese su segundo digito: "))
lado_3 = float(input("Ingrese su tercer digito: "))

if lado_1 < (lado_2 + lado_3) and lado_3 < (lado_1 + lado_2) and lado_2 < (lado_3 + lado_1):
    print("Los digitos ingresados forman un triangulo")
else:
    print("Los lados no forman un triangulo")

if lado_1 == lado_2 == lado_3:
    print("Su triangulo es Equilatero")
elif lado_1 == lado_2 != lado_3:
    print("Su triangulo es Isoceles")
elif lado_1 != lado_2 != lado_3:
    print("Su triangulo es Escaleno")
else:
    print("No es un triangulo")