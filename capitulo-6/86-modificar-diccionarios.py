usuario = {"nombre":"Fede" ,"edad":15,"pais":"Guatemala"}

usuario["telefono"] = 25681234
print(usuario)

usuario["edad"] = "16"
print(usuario)

usuario.update({"telefono":"+502 4766 0639","edad":"16"})
print(usuario)