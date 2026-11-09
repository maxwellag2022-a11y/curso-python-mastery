'''
Demuestre que si dispara una bala y deja caer una canica
al suelo desde la misma altura, ambas tardaran la misma
el ismo tiempo en caer
'''

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def __str__(self):
        return f'({self.x}, {self.y})'

    def __repr__(self):
        return f'Vector : ({self.x}, {self.y})'

    def __add__(self, otro):
        return Vector(self.x + otro.x, self.y + otro.y)

    def __sub__(self, otro):
        return Vector(self.x - otro.x, self.y - otro.y)

    def __eq__(self, otro):
        return self.x == otro.x and self.y == otro.y

    def __len__(self):
        return int((self.x **2 + self.y **2)**0.5)

v1 = Vector(3, 4)
v2 = Vector(1, 2)

print (v1)
print (v2)
print (v1 + v2)
print (v1 - v2)
print(v1 == Vector(3, 4))
print(v1 == v2)
print(v1 != v2)