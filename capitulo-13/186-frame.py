from tkinter import Tk, Label, Button, Frame

ventana = Tk()
cabecera = Frame(ventana, bg="#065f46", height=50)
cabecera.pack(fill="x")
Label(
    cabecera,
    text="ACADEMIA FIBONACCI",
    fg="white",
    bg="#065f46",
    font=("Arial", 14, "bold")
).pack(pady=10)

cuerpo = Frame(ventana, bg="white")
cuerpo.pack(fill="both", expand="yes", pady=10, padx=10)
Label(cuerpo, text="Contenido", bg="white").pack(pady=10)

ventana.mainloop()
