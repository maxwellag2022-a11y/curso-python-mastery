def sumar(*numeros):
    total = 0
    for numero in numeros:
        total = total + numero
    return total

print(sumar(1,2))
print(sumar(2,3,4))
print(sumar(3,4,5))
print(sumar(10,20,30,40,50,60,70,80,90))
print(sumar())