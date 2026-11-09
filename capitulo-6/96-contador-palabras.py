texto = "el sol sale por el este y cae por el oeste"
conteo = {}

for palabra in texto.split():
    conteo[palabra] = conteo.get(palabra,0) + 1

print(conteo)

mas_frecuente = max(conteo, key=conteo.get)
print(f" ✅ Mas Frecuente : '{mas_frecuente}' ({conteo[mas_frecuente]}) veces")