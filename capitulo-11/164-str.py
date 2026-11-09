class Producto:
    def __init__ (self, nombre, precio, stock):#constructor de clase, para objeto
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def __str__(self): #metodo para imprimir el objeto - llamado dunders
        return f"{self.nombre} - {self.precio:.2f} - stock: {self.stock}"

p1 = Producto("Laptop HP", 8500, 12)
print(p1)
    