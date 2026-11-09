def saludar(saludo,*args):
    for nombre in args:
        print(f"{saludo}, {nombre}")

saludar("Hola", "Fede", "Daniel", "Marcos")

    