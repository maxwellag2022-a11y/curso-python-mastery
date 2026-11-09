edad = 25
tiene_licencia = True
tiene_carro = False

puede_manejar = edad >=18 and tiene_licencia
print(puede_manejar)

necesita_uber = not tiene_carro
print(necesita_uber)

va_a_la_fiesta = tiene_carro or tiene_licencia
print(va_a_la_fiesta)
