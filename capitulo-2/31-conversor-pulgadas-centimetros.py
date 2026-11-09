PULGADA_CM = 2.54

try:
    pulgadas = float(input("Ingrese la cantidad de pulgadas: "))
    cm = pulgadas * PULGADA_CM
    print(f"{pulgadas} pulgadas son {cm:.2f} centimetros")
except ValueError:
    print("Ese no es un numero valido")