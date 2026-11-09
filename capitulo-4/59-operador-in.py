expresiones = ["x", "2x", "x+2", "3x+6","5x²+6"]

print("x" in expresiones)
print("x-2" in expresiones)
print("x-2" not in expresiones)

if "x" in expresiones:
    print("Tenemos una expresion lineal")