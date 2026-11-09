# computadora juega con lista ("Piedra", "Papel", "Tijera")
# para que sea al azar puede utilizar Choice
# Utilizar tres botones para piedra Papel o tijera
# utilizar condicionales(if) para saber el resultado sucedio
# puede utilizar una isla de resultados con Frame
# podemos utilizar grilla para posicionar botones y resultados
# podemos utilizar variables vinculadas para el puntaje
# messagebox dialogos del sistema

from tkinter import Tk, Label, StringVar, messagebox, Frame, Button
from random import choice

opciones = ["piedra", "papel", "tijera"]

ventana = Tk()
ventana.geometry("420x420")
ventana.title("Piedra, Papel o Tijera")

puntos_jugador = StringVar(value="0")
puntos_compu = StringVar(value="0")
mensaje = StringVar(value= "Elije tu jugada")

cabecera = Frame(ventana, bg="#065f46", height =50)
cabecera.pack(fill="x")
Label(
    cabecera,
    text="PIEDRA, PAPEL O TIJERA",
    fg="#ffffff",
    bg="#065f46",
    font=("Arial", 14, "bold"),
).pack(pady=10)

def jugar(eleccion):
    compu = choice(opciones)
    if eleccion == compu:
        texto = f"Empate: ambos eligieron {eleccion}"
    elif (eleccion == "piedra" and compu == "tiejra") or (eleccion == "papel" and compu == "piedra") or (eleccion == "tijera" and compu == "papel"):
        texto = f"Ganaste: {eleccion} le gana a {compu}"
        actual = int(puntos_jugador.get())
        puntos_jugador.set(str(actual+1))
    else:
        texto = f"Perdiste: {compu} le gana {eleccion}"
        actual = int(puntos_compu.get())
        puntos_compu.set(str(actual+1))

    mensaje.set(texto)

    if int(puntos_jugador.get()) == 3:
        messagebox.showinfo("Fin del Juego", "Ganaste la partida")
        reiniciar()
    elif int(puntos_compu.get()) ==3:
        messagebox.showwarning("Fin del Juego", "La computadora gano la partida")
        reiniciar()

def reiniciar():
    puntos_jugador.set("0")
    puntos_compu.set("0")
    mensaje.set("Elije tu jugada")


zona_botones = Frame(ventana)
zona_botones.pack(pady=20)

Button(
    zona_botones,
    text="Papel",
    command=lambda: jugar("papel"),
    bg="#10b981",
    fg="white",
    font=("Arial", 12, "bold"),
    width="8"
).grid(row=0, column=0, pady=5, padx=5)

Button(
    zona_botones,
    text="Tijera",
    command=lambda: jugar("tijera"),
    bg="#10b981",
    fg="white",
    font=("Arial", 12, "bold"),
    width="8"
).grid(row=0, column=1, pady=5, padx=5)

Button(
    zona_botones,
    text="Piedra",
    command=lambda: jugar("piedra"),
    bg="#10b981",
    fg="white",
    font=("Arial", 12, "bold"),
    width="8"
).grid(row=0, column=2, pady=5, padx=5)

resultados = Frame(ventana, bg="#d1fae5")
resultados.pack(fill="both", expand="yes", pady=10, padx=10)

Label(
    resultados,
    textvariable=mensaje,
    font=("Arial",12),
    fg="#065f46",
    bg="#d1fae5",
).grid(row=0, column=0, columnspan=2, pady=5, padx=5)

Label(resultados, text="Tu puntaje", bg="#d1fae5").grid(row=1, column=0, pady=5, padx=30)
Label(resultados, text="Computadora", bg="#d1fae5").grid(row=1, column=1, pady=5, padx=30)

Label(resultados, textvariable=puntos_jugador, bg="#d1fae5", font=("Arial",32)).grid(row=2, column=0, pady=5, padx=30)
Label(resultados, textvariable=puntos_compu, bg="#d1fae5", font=("Arial",32)).grid(row=2, column=1, pady=5, padx=30)


ventana.mainloop()





