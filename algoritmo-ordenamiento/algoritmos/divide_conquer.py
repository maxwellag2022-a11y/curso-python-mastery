lista = [6,5,3,1,8,7,2,4]

def mezclar(izquierda, derecha):
''' Une dos listas YA ordenadas en una sola lista
ordenada'''

    resultado = []
    i=j=0
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] <= derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1

    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    return resultado

def ordenar(lista):

    if len(lista) <= 1:
        return lista[:]

    medio = len(lista) // 2
    izquierda = lista[:medio]
    derecha = lista[medio:]

    izq_ordenada = ordenar(izquierda)
    der_ordenada = ordenar(derecha)

    return izq_ordenada + der_ordenada
print(ordenar(lista))

    