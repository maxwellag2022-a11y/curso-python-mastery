cuadrados = {n:n**2 for n in range(1,6)}
print(cuadrados)

notas = {"Luis":85, "Maria":92, "Pedro":78,"Ana":55}
inverso = {v:k for k,v in notas.items() }
print(inverso)

aprobados = {k:v for k,v in notas.items() if v >=60}
print(aprobados)

texto = "fibonacci"
conteo = {letra : texto.count(letra) for letra in set(texto)}
print(conteo)