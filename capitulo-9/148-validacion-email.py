'''
emails=[
    "Luis@gmail.com.gt" -> true
    "no-arroba"
    "doble@@arroba.com"
    "@domino.com"
    "usuario@inpunto
]

crear una funcion que se llame es_valdido(texto)
retornara verdadero si es valido

for para que tome a todos los emails y diga cuales son validos
hacer varios if con early return
'''

emails =[
    "Luis@gmail.com.gt",
    "no-arroba",
    "doble@@arroba.com",
    "@domino.com",
    "usuario@inpunto"
]

def es_valido(texto):

    if texto.count("@") != 1:
        return "No es un correo valido"
    nombre, dominio = texto.split("@")
    if not nombre or not dominio:
        return "No es un correo valido"
    if "." not in dominio:
        return "No es un correo valido"

    return "Es un correo valido"

for email in emails:
    print(email,es_valido(email))



