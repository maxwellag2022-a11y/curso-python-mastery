import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment

estudiantes = [
    ("Luis Castillo",85,92,78),
    ("Maria Lopez",90,85,95),
    ("Pedro Garcia",65,70,58),
    ("Allan Martinez",88,82,79),
    ("Juan Hernandez", 55,60,50)
   ]

wb = openpyxl.Workbook()
hoja = wb.active
hoja.tittle = "Notas 2026"

encabezados = ["Estudiante", "Parcial 1", "Parcial 2", "Parcial 3", "Promedio", "Resultado"]
hoja.append(encabezados)

fuente = Font(name="Arial", size=12, bold=True, color="FFFFFF")
relleno = PatternFill(start_color='065f46', end_color='065f46',fill_type='solid')
centro = Alignment(horizontal="center")

for i, _ in enumerate(encabezados, start=1):
    celda = hoja.cell(row=1, column=i)
    celda.font = fuente
    celda.fill = relleno
    celda.alignment = centro

for nombre, p1, p2, p3 in estudiantes:
    promedio = (p1 + p2 + p3)/3
    resultado = "APROBADO" if promedio >= 60 else "REPROBADO"
    hoja.append([nombre,p1,p2,p3, promedio, resultado])

verde = PatternFill(start_color='D1FAE5', end_color='D1FAE5',fill_type='solid')
rojo = PatternFill(start_color='FEE2E2', end_color='FEE2E2',fill_type='solid')

for fila in range(2,len(estudiantes)+2):
     resultado = hoja.cell(row=fila, column=6).value
     color = verde if resultado == "APROBADO" else rojo
     for column in range(1,8):
         hoja.cell(row=fila, column=column).fill = color


wb.save("Reporte_notas_2026.xlsx")
print("Reporte Generado!")