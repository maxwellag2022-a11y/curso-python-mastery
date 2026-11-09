inventario = ["mouse", "teclado", "monitor", "laptop", "tablet"]

print(f" ✅ Original: {inventario}")

inventario.append("Auriculares")

print(f" ✅ Tras Agregar: {inventario}")

inventario.pop(1)

print(f" ✅ Tras Eliminar: {inventario}")

inventario.sort()

print(f" ✅ Ordenado: {inventario}")
print(f" ✅ Total: {len(inventario)} productos")