expresiones = ["x", "2x", "x+2", "3x+6","5x²+6"]

for expresion in expresiones:
    print(expresion)

for i, expresion in enumerate(expresiones):
    print(f"{i} - {expresion}")

for i in range(len(expresiones)):
    print(f"{i} - {expresiones[i]} ✅")