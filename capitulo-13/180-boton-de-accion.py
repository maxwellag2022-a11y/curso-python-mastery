from tkinter import Tk, Button, Label

def Saludar(nombre):
   print(f"Hola {nombre}!")

ventana = Tk()

boton = Button(
    ventana,
    text="Saludar",
    command=lambda: Saludar("Fede"),
    bg="#10b981",
    fg="white",
    font=("Arial", 12,"bold")
)


boton.pack(pady=20)

ventana.mainloop()