def sumar(a,b,c):
    return a+b+c

numeros = [1,2,3]
print(sumar(*numeros))

datos = {"a":10,"b":20,"c":30}
print(sumar(**datos))