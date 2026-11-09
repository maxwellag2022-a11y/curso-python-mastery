import json

#Diccionario a string JSON
usuario = {"nombre":"Fede","edad":15,"sexo":"Masculino"}
texto_json = json.dumps(usuario, indent=4)
print(texto_json)

#string JSON a Diccionario

crudo = '{"nombre":"Aldara","edad":14,"sexo":"Femenino"}'
parsed = json.loads(crudo)
print(crudo)

with open("usuario.json", "w") as f:
    json.dump(usuario,f,indent=3)

with open("usuario.json","r") as f:
    cargado = json.load(f)

print(cargado)