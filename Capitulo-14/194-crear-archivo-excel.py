import openpyxl

wb = openpyxl.Workbook()

hoja = wb.active
hoja.tittle = "Inventario"

hoja["A1"] = "Producto"
hoja["B1"] = "Precio"
hoja["C1"] = "Stock"

hoja.cell(row = 2, column = 1, value = "Laptop HP")
hoja.cell(row = 2, column = 2, value = 8500)
hoja.cell(row = 2, column = 3, value = 12)

hoja.append(["Teclado Mecanico",350.00,28])
hoja.append(["Monitor 24",2160,25])


wb.save("Inventario.xlsx")
print("Archivo Guardado")