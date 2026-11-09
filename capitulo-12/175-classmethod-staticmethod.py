class Fecha:

    def __init__(self, dia, mes, anio):
        self.dia = dia
        self.mes = mes
        self.anio = anio

    @classmethod
    def desde_string(cls, fecha_str):
        '''Constructur alternativo desd DD/MM/YYYY'''
        d,m,a = map(int, fecha_str.split('/'))
        return cls(d,m,a)

    @staticmethod
    def es_bisiesto(anio):
        return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

    def __str__(self):
        return f'{self.dia}/{self.mes}/{self.anio}'

fecha1 = Fecha(7, 3, 2011)
fecha2 = Fecha.desde_string("25/12/2025")

print(fecha1)
print(fecha2)

print(Fecha.es_bisiesto(2004))