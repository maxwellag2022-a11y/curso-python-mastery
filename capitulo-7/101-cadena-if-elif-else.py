nota = int(input("Ingrese su nota: "))

if nota >= 90:
    letra = "A"
elif nota >= 80:
    letra = "B"
elif nota >= 70:
    letra = "C"
elif nota >= 60:
    letra = "D"
else :
    letra = "F"

print(f"Tu calificacion es {letra}")