def crear_perfil(**datos):
    print("=== Perfil ===")
    for clave, valor in datos.items():
        print(f"{clave}: {valor}")

crear_perfil(nombre="Fede", edad=15, ciudad="Guatemala")
crear_perfil(nombre="Marcos", edad=16, ciudad="Guatemala")