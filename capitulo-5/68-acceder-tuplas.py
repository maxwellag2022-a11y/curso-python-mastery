persona = ("Fede",15,"Guatemala","desarollador")

print(persona[0])
print(persona[-1])
print(persona[1:3])
print(len(persona))

# esto no se puede > persona[0] = "Maria"

nueva_persona = ("Maria",) + persona[1:]
print(nueva_persona)