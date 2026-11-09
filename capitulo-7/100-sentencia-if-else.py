edad = int(input("Digite su edad: "))

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
    print(f" Te faltan {18 - edad} años")