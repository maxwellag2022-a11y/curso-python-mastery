while True:
    try:
        numero = int(input("Ingresa un numero entero: "))
        print(f"El doble es {numero * 2 }")
        print(f"El cuadrado es {numero ** 2}")
        print(f"Es par? {numero % 2 == 0}")
    except ValueError:
        print("Eso no parece un numero entero valido")
        print("Volver a correr el programa")