'''
Escribe una funcion (puedes ponerle cualquier nombre)
que reciba cualquier palabra com parametro y que
desenvuelca todas sus letras unicas (sin repetir) pero
en orden alfabetico
'''

def letras(string):
  return sorted(set(list(string)))


string = input("ingrese palabra: ")
print(f"las letras separadas de la palabra son: {letras(string)}")