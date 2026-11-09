#Dadu un año, decir si es bisiesto
#bisiesto si es divisible por 4
#Excepto si es divisible por 100
#a menos que tambien sea divisible por 400

año = int(input("Ingrese un año: "))

if año % 400 == 0:
    print(f"{año} Es un año bisiesto")
elif año % 100 == 0:
    print(f"{año} No es un año bisiesto")
elif año % 4 == 0:
    print(f"{año} #s un año bisiesto")
else:
    print("No es un año bisiesto")

es_bisiesto = (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0)
print(f"{año} es {es_bisiesto}")