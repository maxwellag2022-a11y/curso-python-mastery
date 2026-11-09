#reglas : computadora piense un numero "Hardcodeado" -> random
# empezar un ciclo -> ciclo while
# while True:
# si el numero es muy grande dira tu numero es muy grande intenta con uno mas pequeño
# si el numero es muy peqieño dira tu numero es muy pequeño intenta con uno mas grande
# puede utilizar emojis
# vidas entonces el while true seria mejor while  vidas >=0
import random

numero = random.randint(1, 100)
print("="*35)
print(f"{'ADIVINA EL NUMERO':^35}")
print("="*35)
#print(f"El numero es {numero}")
VIDAS = [
    "❤️❤️❤️❤️❤️❤️",
    "🖤❤️❤️❤️❤️❤️",
    "🖤🖤❤️❤️❤️❤️",
    "🖤🖤🖤❤️❤️❤️",
    "🖤🖤🖤🖤❤️❤️",
    "🖤🖤🖤🖤🖤❤️",
    "🖤🖤🖤🖤🖤🖤",
]
vidas = 0
MAX_VIDAS = 6

while vidas < MAX_VIDAS:
    print(VIDAS[vidas])
    intento = int(input(f"{'¿en que numero estoy pensando?':^35}: "))
    if intento <= 0 or intento > 100:
        print("el numero es invalido")
    else:
            if intento == numero:
                print(f" ✅ El intento es correcto! el numero es {numero}")
                break
            elif intento < numero:
                print("❌ El intento es incorrecto, el numero es mayor al ingresado")
                print(f"Errores: {vidas + 1} de {MAX_VIDAS} errores")
                vidas += 1
            elif intento > numero:
                print("❌ El intento es incorrecto, el numero es menor al ingresado")
                print(f"Errores: {vidas + 1} de {MAX_VIDAS} errores")
                vidas += 1
print("="*35)


