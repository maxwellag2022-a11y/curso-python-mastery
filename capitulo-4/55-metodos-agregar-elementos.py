expresiones = ["x", "2x", "x+2", "3x+6","5x²+6"]

 #append lo añade al final
expresiones.append("4x-9")
print(expresiones)

#insert añade los datos en el index (indice) escogido
expresiones.insert(4,"-10+x")
print(expresiones)

#añade pro medio de metodo LIFO
expresiones.extend(["5x","9x+8"])
print(expresiones)

expresiones += ["9x+7","9x+5"]
print(expresiones)