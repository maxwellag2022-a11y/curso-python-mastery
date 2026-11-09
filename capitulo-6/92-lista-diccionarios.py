estudiantes = [
    {"nombre":"Fede", "nota":85, "aprobado": True},
    {"nombre": "Daniel", "nota": 92, "aprobado": True},
    {"nombre": "Marcos", "nota": 59, "aprobado": False},
    {"nombre": "Marialuisa", "nota": 89, "aprobado": True},

]

for estudiante in estudiantes:
    estado = "✅" if estudiante["aprobado"] else "❌"
    print(f"{estado} {estudiante['nombre']:<10}{estudiante["nota"]:>5}")

aprobado = [e for e in estudiantes if e["aprobado"]]
print(f"\nAprobados: {len(aprobado)}")

promedio = sum(e["nota"] for e in estudiantes) / len(estudiantes)
print(f"Promedio: {promedio}")