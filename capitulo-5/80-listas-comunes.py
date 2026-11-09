tomados = ["Python", "Algoritmos","SQL","GIT"]
oferta_semestre = ["Python", "Django", "Docker", "SQL", "AWS"]


semestre_a = set(tomados)
semestre_b = set(oferta_semestre)

comunes = semestre_a.intersection(semestre_b)
nuevos = semestre_b - semestre_a

print(" ✅ Cursos que puede revalidar: ", sorted(comunes))
print(" ✅ Cursos nuevos disponibles: ", sorted(nuevos))


