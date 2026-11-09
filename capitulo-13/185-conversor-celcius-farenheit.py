from tkinter import Tk, Label, Entry, Button

ventana = Tk()
ventana.geometry("350x400")
ventana.title("Conversor de temperatura")

Label(ventana, text="Temperatura: ").pack(pady=10)
entrada = Entry(ventana, font=("Arial", 14), width=30)
entrada.pack(pady=10)

def convertir(origen):
    valor = float(entrada.get())

    if origen == "C":
        resultado = valor * 9/5 + 32
        mensaje = f"{valor}C = {resultado:.2f}F"
    else:
        resultado = (valor - 32) * 5/9
        mensaje = f"{valor}F = {resultado:.2f}C"

    Label(ventana, text=mensaje,fg="#10b981").pack(pady=10)

Button(
    ventana,
    text="Celcius a Farenheit",
    command=lambda: convertir("C"),
    bg="#10b981",
    fg="white",
    font=("Arial", 12, "bold"),
).pack(pady=10)

Button(
    ventana,
    text="Farenheit a Celcius",
    command=lambda: convertir("F"),
    bg="#10b981",
    fg="white",
    font=("Arial", 12, "bold"),
).pack(pady=10)

ventana.mainloop()