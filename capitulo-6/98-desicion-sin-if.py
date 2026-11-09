#Prguntar una edad
#Decidir: (No utilizaremos if ni for)
#Puede beber
#Puede entrar
#Tiene entrada gratis
#A una discoteca
#18 pueden beber, pueden entrar
#30 no pueden entrar a discotecas
#20 y 25 tienen entrada gratis
#flujo preguntar edad -> escribir las tres respuestas


edad = int(input("¿Cual es tu edad?:"))

puede_entrar = (bool(edad >= 18 and edad < 30))
puede_beber = (bool(edad >= 18))
entrada_gratis = (bool(edad == 20 or edad == 25))

respuestas = {True:"Si ✅ ", False:"No ❌ "}

print(f"¿Puede entrar a la discoteca?: {respuestas[puede_entrar]}")
print(f"¿Puede beber?: {respuestas[puede_beber]}")
print(f"¿Tiene entrada gratis?: {respuestas[entrada_gratis]}")


