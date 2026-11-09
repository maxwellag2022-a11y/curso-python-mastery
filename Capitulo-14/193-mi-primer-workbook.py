import openpyxl

wb = openpyxl.Workbook()

hoja = wb.active

print(hoja.title)