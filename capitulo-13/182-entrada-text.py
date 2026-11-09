from tkinter import Tk, Entry, Button, Label

ventana = Tk()
ventana.geometry("300x300")
ventana.title("Formulario")

Label(ventana, text="Tu nombre: ").pack()
entrada = Entry(ventana, font=("Arial",14), width=30)
entrada.pack()

def saludar():
    nombre = entrada.get()
    Label(ventana, text=f"Hola {nombre}!", fg="#10b981").pack()

Button(ventana, text="Enviar", command=saludar).pack(pady=10)

ventana.mainloop()