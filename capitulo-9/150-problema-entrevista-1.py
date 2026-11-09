'''
 crea una funcion llamadadevolver_distintos() que reciba 3 integerrs como parametros

 si la suma de los 3 numeros es mayor a 15, va a devolver el numero mayor

 si la suma de los 3 numeros es menor a 10, vaa devolver el numero menonr

 si la suma de los 3 numeros es un valor entre 10 y 15 (incluidos), va a devolver el numero intermedio
'''

def devolver_distintos(numeros):
    if not numeros:
        return None
    elif sum(numeros) < 10:
        return min(numeros)
    elif sum(numeros) > 15:
        return max(numeros)
    else:
        return sum(numeros) - min(numeros) - max(numeros)


valor_1 = int(input("ingrese su primer valor: "))
valor_2 = int(input("ingrese su segundo valor: "))
valor_3 = int(input("ingrese su tercer valor: "))

numeros = [valor_1, valor_2, valor_3]

print(f"el valor es: {devolver_distintos(numeros)}")

