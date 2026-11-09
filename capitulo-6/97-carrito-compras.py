carrito_compras = [
    {"producto":"laptop","precio":8500.00,"cantidad":1},
    {"producto": "mouse", "precio": 125.50, "cantidad": 2},
    {"producto": "Teclado", "precio": 320.00, "cantidad": 1},
    {"producto": "cable", "precio": 45.00, "cantidad": 3},

]

print(f"{'PRODUCTO':<15}{'PRECIO':>10}{'CANT':>6}{'SUB':>12}")
print("-"*43)

total = 0

for item in carrito_compras:
    sub = item["precio"] * item["cantidad"]
    total += sub
    print(f"{item['producto']:<15}{item['precio']:>10}{item['cantidad']:>6}{sub:>12}")

print("-" * 43)
print(f"{'TOTAL':<31}Q.{total:>11}")


