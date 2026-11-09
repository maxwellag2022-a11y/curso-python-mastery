agenda = {
    "Fede":"+502 4736-3311",
    "Daniel":"+502 8547-6152",
    "Marcos":"+502 3274-9156",
    "Marilu":"+502 7745-6348"
}

nombre = input("Ingrese su nombre: ").strip().title()
telefono = agenda.get(nombre, "No encontrado")
print(f" ✅ {nombre}: {telefono}")

nuevo_nombre = input("Ingrese su nombre: ").strip().title()
nuevo_telefono = input("Ingrese su telefono: ").strip()
agenda[nuevo_nombre] = nuevo_telefono

print("\n 💻 Agenda completa: ")
for n, t in sorted(agenda.items()):
    print(f" ✅ {n}: {t}")