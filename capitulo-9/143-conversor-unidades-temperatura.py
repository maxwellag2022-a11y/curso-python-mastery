# crea dos funciones: una que convierta de celcius a farenheit, y otra que convierta a celcius a farenheit
# hacerlo con input
# fahrenheit a celcius -> return

# celcius a farenheit -> return

# input oara mostrar ambos o dos prints

# intput que reciba en una variable: grados = float(input(...
# llamar a funcion con la variable como parametro

def temperaturas(celcius):
    return f"su temperatura ingresada en celcius equivale a: {celcius * 1.8 + 32} grados de farenheit"

celcius = temperaturas(int(input("ingrese su temperatura en celcius: ")))

def temperaturas(farenheit):
     return f"su temperatura ingresada en farenheit equivale a: {(farenheit - 32)*5/9} grados de celcius"

farenheit = temperaturas(int(input("ingrese su temperatura en farenheit: ")))

print("celcius:",celcius)
print("farenheit: ", farenheit)
