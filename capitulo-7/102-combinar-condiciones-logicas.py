edad = int(input("Digite su edad: "))
tiene_licencia= input("Tiene licencia? (s/n)").lower() == "s"

if edad >=18 and tiene_licencia:
    print("Puede manejar")

if edad <18 or not tiene_licencia:
    print("No puede manejar")

if 18 <= edad <= 65:
    print("Edad laboral activa")

if edad in range(18,66):
    print("Edad laboral activa")

