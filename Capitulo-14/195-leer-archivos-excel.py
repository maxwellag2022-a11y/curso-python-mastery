import openpyxl

wb = openpyxl.load_workbook("Inventario.xlsx")
hoja = wb.active

print(f"Hoja: {hoja.title}")
print(f"Filas: {hoja.max_row}")
print(f"Columnas: {hoja.max_column}")

print(hoja["A1"].value)
print(hoja.cell(row=2, column=1).value)

for fila in hoja.iter_rows(values_only=True):
    print(fila)

fila = hoja.iter_rows(values_only=True)
encabezado = next(fila)
print("Columnas: ",encabezado)

for producto, precio, stock in fila:
    print(f"{producto:<25}: Q.{precio:>8.2f} ({stock} en stock)")
    