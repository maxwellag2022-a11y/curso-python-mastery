from tkinter import Tk, Button, Label

def Saludar(nombre):
    mensaje = f"Hola {nombre}!"
    Label(ventana, text=mensaje).pack()

ventana = Tk()

boton = Button(
    ventana,
    text="Saludar",
    command=lambda: Saludar("Fede"),
    bg="#10b981",
    fg="white",
    font=("Arial", 12,"bold")
)


boton.pack(pady=10)
ventana.mainloop()