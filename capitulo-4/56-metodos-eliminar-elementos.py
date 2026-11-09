expresiones = ["x", "2x", "x+2", "3x+6","5x²+6"]

expresiones.remove("2x")
print(expresiones)

ultimo = expresiones.pop()
print(expresiones)
print(ultimo)

segundo = expresiones.pop(1)
print(segundo)
print(expresiones)

del expresiones[0]
print(expresiones)

expresiones.clear()
print(expresiones)