notas = []
while True:
    entrada = input("Ingrese una nota (o 'fin para terminar'): ").strip()
    if entrada.lower() == "fin":
        break
    try:
        nota = float(entrada)
        notas.append(nota)
    except ValueError:
        print(f" ❌ Numero invalido. intenta de nuevo")

if notas:
   promedio = sum(notas) / len(notas)
   print(f"\nNotas:{notas} \nPromedio: {promedio}")
else: print("No hay notas")