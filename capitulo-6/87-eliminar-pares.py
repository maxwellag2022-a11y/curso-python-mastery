usuario = {"nombre":"Fede" ,"edad":15,"pais":"Guatemala"}

del usuario["nombre"]
print(usuario)

edad = usuario.pop("edad")
print(edad)
print(usuario)

tel = usuario.pop("telefono","no registrado")
print(tel)

usuario.clear()
print(usuario)