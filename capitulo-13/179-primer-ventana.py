from tkinter import Tk, Label

ventana = Tk()

ventana.title("Mi primer Ventana")
ventana.geometry("400x300")

etiqueta = Label(
    ventana,
    text="Hola, desde Tkinter!",
    font=("Times New Roman", 18),
    fg="#065f46",
    bg="#d1fae5"
)

etiqueta.pack(pady=10)

ventana.mainloop()

