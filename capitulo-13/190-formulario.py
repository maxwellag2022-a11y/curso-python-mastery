from tkinter import Tk, Label, Entry, Button, StringVar, messagebox

ventana = Tk()
ventana.title("Registr")
ventana.geometry("400x300")
ventana.configure(bg="#f8fafc")

EMERALD = "#108981"
SLATE = "#1E293B"

Label(ventana,
      text="REGISTRO DE USUARIO",
      bg="#065f46",
      fg="White",
      font=("Arial", 14, "bold"),
      padx=10
      ).pack(fill="x")



nombre_var = StringVar()
email_var = StringVar()
edad_var = StringVar()

frame = Label(ventana, bg="#f8fafc")
frame.pack(pady=20)

Label(frame,
      text= "Nombre",
      bg="#f8fafc"
      ).grid(row=0, column=0, sticky="e")
Entry(frame, textvariable=nombre_var,width=25
      ).grid(row=0, column=1, sticky="e", pady=5)

Label(frame,
      text= "Email",
      bg="#f8fafc"
      ).grid(row=1, column=0, sticky="e")
Entry(frame, textvariable=email_var,width=25
      ).grid(row=1, column=1, sticky="e", pady=5)

Label(frame,
      text= "Edad",
      bg="#f8fafc"
      ).grid(row=2, column=0, sticky="e")
Entry(frame, textvariable=edad_var,width=25
      ).grid(row=2, column=1, sticky="e", pady=5)

def registrar():
    nombre = nombre_var.get().strip()
    email = email_var.get().strip()
    edad = edad_var.get().strip()

    datos = [nombre, email, edad]

    if not nombre or not email or not edad:
        messagebox.showwarning("Faltan datos", "Complete todos los campos")
        return

    if not edad.isdigit():
        messagebox.showwarning("Error", "La edad debe ser numerica")
        return

    messagebox.showinfo("Exito", f"Registro: {datos[0]} ({datos[2]} años)" )

    nombre_var.set("")
    email_var.set("")
    edad_var.set("")

Button(ventana, text="Registrar",
       command=registrar,
       bg=EMERALD,
       fg="white",
       font=("Arial",12,"bold")
       ).pack(pady=10)
ventana.mainloop()

