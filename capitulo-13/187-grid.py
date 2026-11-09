from tkinter import Tk, Label, Button, Entry

ventana = Tk()
ventana.geometry("800x600")
Label(ventana, text="Nombre").grid(row=0, column=0, padx=5, pady=5)
Entry(ventana).grid(row=0, column=1, padx=5, pady=5)
Label(ventana, text="Email").grid(row=1, column=0, padx=5, pady=5)
Entry(ventana).grid(row=1, column=1, padx=5, pady=5)
Button(ventana, text="Enviar").grid(row=2, column=0, columnspan=2, padx=5, pady=5)

Label(ventana, text="Posicionado").place(x=370, y=300)

ventana.mainloop()