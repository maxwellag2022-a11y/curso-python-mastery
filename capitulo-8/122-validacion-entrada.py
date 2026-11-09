edad = -1
while edad <= 0:
    try:
        edad = int(input("Ingrese su edad: "))
        if edad <= 0:
            print("Ingrese un numero valido (Edad debe de ser positiva)")
    except ValueError:
        print("Tiene que ser un numero valido")

print(f"Edad registrada: ✅ {edad}")