edad = 24

#if edad >= 18:
#    estado = "mayor"
#else:
#    estado = "menor"

estado = "Mayor" if edad >= 18 else "Menor"

print(estado)

hora = 15

saludo = "Buen dia" if hora < 12 else "Buena tarde" if hora < 18  else "Buena noche"

print(saludo)

puntaje = 89

nota_letra = "A" if puntaje >= 90 else "B" if puntaje >= 80 else "C" if puntaje >= 70 else "D"

print(nota_letra)