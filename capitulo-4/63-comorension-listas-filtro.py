#filtro
pares = [n for n in range(20) if n % 2 == 0]
print(pares)

#transformacion
nombre = ["luis", "maria", "pedro"]

capitalizado = [n.title() for n in nombre]
print(capitalizado)

#filtrado y transformacion
notas = [68,72,85,90,55,70]
aprobados = [n for n in notas if n >= 60]
print(aprobados)

expresiones = ["5+2*6", "10*9-20", "-50+6*1+10"]
resultados = [eval(n) for n in expresiones if eval(n) < 0]
print(resultados)

aprobados = ["Aprobado ✅" if n >= 60 else "Reprobado ❌" for n in notas]
print(aprobados)