'''
 deg crear_usuario(nombre,email,**extras)

 crear una funcion que cree un perfil de usuario con campos
 arbitriarios y valide algunos campos obligatorios

 usuario ={
  "nombre":nombre
  "email":email
  ....

  crear variables que sean los fijos y los extras y cin un for que los imprima
  .update(extras)
'''

def crear_usuario(nombre,email,**extras):
    usuario = {
      "nombre":"Flavia",
      "email":"f@gmail.com"
    }
    usuario.update(extras)
    return usuario
u = crear_usuario(nombre="Flavia",email="f@gmail.com", edad = 15, genero="feminino")
for clave, valor in u.items():
    print(f"{clave}: {valor}")

