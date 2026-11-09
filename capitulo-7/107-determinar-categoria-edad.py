# bebe : 0 - 2, niño : 3-12, adolescente 13-17, adulto : 18 - 64, adulto mayor : 65+

edad = int(input("Ingrese su edad: "))
if 0<=edad<=2:
    print("Eres un bebé")
elif 3<=edad<=12:
    print("Eres un niño")
elif 13<=edad<=17:
    print("Eres un adolescente")
elif 18<=edad<=64:
    print("Eres un adulto")
elif edad>=65:
    print("Eres un adulto mayor")
else:
    print("Edad invalida")


try:
    Edad = int(input("Ingrese su edad: "))

    if int(Edad) < 0:
        print("No se puede agrerar edades negativas")
    elif int(Edad) <= 2:
        print("Bebé")
    elif int(Edad) <= 12:
        print("Niño")
    elif int(Edad) < 18:
        print("Adolescente")
    elif int(Edad) <= 64:
        print("Adulto")
    elif int(Edad) > 64:
        print("Adulto mayor")
    else:
        print("Ingrese una edad valida")
except ValueError:
    print("Ingrese una edad valida")
