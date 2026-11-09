def calcular_imc(peso_kg, altura_a):
    '''
    Calcular el Indice de mas a corporal (IMC)

    Argumentos:
        peso_kg: Peso del paciente float
        altura_a: Altura del paciente en float

    retorna:
    float: el IMC redondeado a 2 decimales
    '''

    return round(peso_kg / (altura_a ** 2), 2)

print(calcular_imc(45,1.65))
help(calcular_imc)
print(calcular_imc.__doc__)