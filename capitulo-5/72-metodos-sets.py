colores = {"#FF0000", "#00FF00", "#0000FF"}

colores.add("#FFFFFF")
print(colores)

colores.add("#000000")
print(colores)

colores.remove("#00FF00")
print(colores)

colores.remove("#FFFFFF")
print(colores)

for color in colores:
    print(color)