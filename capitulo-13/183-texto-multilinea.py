from tkinter import Tk, Text, END

ventana = Tk()
area = Text(ventana, font=("Consolas",11), height = 10, width =50)
area.pack(pady=10, padx=10)
area.insert(END, "Escribe tu nota aqui")

ventana.mainloop()
