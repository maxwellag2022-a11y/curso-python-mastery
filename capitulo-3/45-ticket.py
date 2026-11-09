producto_1 = ("Mouse",125.50)
producto_2 = ("Teclado",320.00)
producto_3 = ("Audifonos",450.75)

subtotal = producto_1[1] + producto_2[1] + producto_3[1]
iva = subtotal * 0.12
total = subtotal + iva

print("="*35)
print(f"{'ACADEMIA FIBONACCI':^35}")
print("="*35)
print(f"{producto_1[0]:<20}{producto_1[1]:>15}")
print(f"{producto_2[0]:<20}{producto_2[1]:>15}")
print(f"{producto_3[0]:<20}{producto_3[1]:>15}")
print("-"*35)
print(f"{'subtotal:':<20}{subtotal:15}")
print(f"{'IVA (12%):':<20}{iva:>15}")
print(f"{'TOTAL:':<20}{total:>15}")
print("="*35)
