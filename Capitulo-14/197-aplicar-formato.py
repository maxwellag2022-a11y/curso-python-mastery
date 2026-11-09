import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side

wb = openpyxl.Workbook()
hoja = wb.active

hoja ["A1"] = "Producto"
hoja ["B1"] = "Precio (Q)"
hoja ["C1"] = "Stock"

fuente = Font(name="Arial", size=12, bold=True, color="FFFFFF")
relleno = PatternFill(start_color="065f46", end_color="065f46", fill_type="solid")
centro = Alignment(horizontal="center", vertical="center")

for celda in ["A1","B1","C1"]:
    hoja[celda].font = fuente
    hoja[celda].fill = relleno
    hoja[celda].alignment = centro

datos = [
    ("Laptop", 8500, 17),
    ("Mouse", 125, 45),
    ("Teclado", 350, 28)
]

for fila in datos:
    hoja.append(fila)

border_fino = Side(border_style="thin", color="000000")
for fila in hoja ["A1:C4"]:
    for celda in fila:
        celda.border = Border(
            left=border_fino,
            right=border_fino,
            top=border_fino,
            bottom=border_fino
        )
hoja.append(["Total","","=SUM(C2:C4)"])
hoja.append(["Promedio: ", "=AVERAGE(B2:B4)", ""])
wb.save("formato.xlsx")
