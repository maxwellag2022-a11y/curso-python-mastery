import openpyxl

wb = openpyxl.Workbook()

hoja_inv = wb.active
hoja_inv.title = "Inventario2"

hoja_ven = wb.create_sheet("Ventas")
hoja_clientes = wb.create_sheet("Clientes",0)

print(wb.sheetnames)

ws = wb["Inventario2"]
ws["A1"] = "Producto"

del wb["Clientes"]

wb.save("Inventario2.xlsx")
