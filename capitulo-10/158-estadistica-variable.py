'''
Funcion que reciba cualquier cantidad de numeros
y devuelva la suma, promedio y cantidad
'''

def sumar(*numeros):
    total = 0
    for numero in numeros:
        total = total + numero
    return total, total/len(numeros), len(numeros)

print(sumar(10,20,30,40,50,60,70,80,90))