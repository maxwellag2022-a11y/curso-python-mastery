from tkinter import Tk, Entry, Button, Label

ventana = Tk()
ventana.geometry("600x600")
ventana.title("conversor Farenheit a Celscius")

Label(ventana, text="Tu cantidad: ").pack()
cantidad = Entry(ventana, font=("Arial", 14), width=30)
cantidad.pack()

boton1 = Button(
    ventana,
    text="farenheit",
    command=lambda: far_cen(int(cantidad)),
    bg="#10b981",
    fg="white",
    font=("Arial", 12,"bold")
)

boton2 = Button(
    ventana,
    text="celscius",
    command=lambda: cen_far(int(cantidad)),
    bg="#10b981",
    fg="white",
    font=("Arial", 12,"bold")
)

def far_cen(cantidad):
    resultado = (cantidad - 32*5/9)
    Label(ventana, text=resultado).pack()


def cen_far(cantidad):
    resultado = (cantidad * 9/5 + 32)
    Label(ventana, text=resultado).pack()


boton1.pack(pady=10)
boton2.pack(pady=10)

ventana.mainloop()
