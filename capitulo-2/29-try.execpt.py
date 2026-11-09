try:
    edad = int(input("Edad: "))
    print(f"En 10 años tendras {edad + 10}")
except ValueError:
    print("Esto no es un numero valido")