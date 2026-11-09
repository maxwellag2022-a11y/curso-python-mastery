from tkinter import Tk, Label, Button, StringVar

ventana = Tk()
contador = StringVar(value="0")
Label(ventana, textvariable=contador, font=("Arial", 32)).pack(pady=20)

def incrementar():
    actual = int(contador.get())
    contador.set(str(actual + 1))

Button(ventana, text="+1", command=incrementar).pack(pady=20)

ventana.mainloop()