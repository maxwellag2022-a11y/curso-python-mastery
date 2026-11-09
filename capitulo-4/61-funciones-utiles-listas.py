expresiones = ["x", "2x", "x+2", "3x+6","5x²+6"]
numeros = [3,1,4,1,5,9,2,6,5]

print(len(expresiones))
print(sum(numeros))
print(max(numeros))
print(min(numeros))

#promedio = (n1 + n2 + .... + nk) / n
print(sum(numeros) / len(numeros))

ventas = [True, False, True, True]
print(any(ventas))
print(all(ventas))