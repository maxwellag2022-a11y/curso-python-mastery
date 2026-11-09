'''
Escribe una funcion que requiera
una cantidad indefinida de argumentos.
lo que hara que esta funcion es devolver
True si en algun momento se ha ingresado
el numero 0 repetido dos veces consecutivas

por ejemplo:

{5,6,1,0,0,9,3,5} >>> True
{6,0,5,1,3,0,1,} >>> False
'''

def consecutivos(*args):
    i = 0
    for i in  range(len(args)):
        if args[i] == 0 and args [i+ 1] == 0:
            return True
    i +=1

    return False

print(consecutivos(5,6,1,0,0,9,3,5))




