nombre = input("Ingrese su nombre: ").strip()
email = input ("Ingrese su email: ").strip()
telefono = input ("Ingrese su telefono: ").strip()


datos = (nombre, email, telefono)

if all(datos):
    print("Todos los campos completos")
    print(f"Bienvenido {nombre} ({email})")
else:
    print("Hay campos vacios")
    if not nombre:
        print(" ❌ Falta el nombre")
    if not email:
        print(" ❌ Falta el email")
    if not telefono:
        print(" ❌ Falta el telefono")
