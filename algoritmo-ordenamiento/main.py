from algoritmos import ALGORITMOS
import os


def mostrar_menu():
    print("\n===== ALGORITMOS DE ORDENAMIENTO =====")
    for i, clase in enumerate(ALGORITMOS, start=1):
        print(f"{i}. {clase().nombre}")
    print(f"{len(ALGORITMOS) + 1}. Comparar todos")
    print("0. salir")

def leer_lista():
    texto = input("Numeros separados por comas (ENTER = 6,5,3,1,8,7,2,4)")
    if texto.strip() == "" :
        return[6,5,3,1,8,7,2,4]
    return [int(x) for x in texto.split(",")]


def main():
    os.system("color 51")
    while True:
        mostrar_menu()
        opcion = input("Ingrese una opcion: ")

        if opcion == "0":
            print("¡Hasta Luego!")
            break

        if not opcion.isdigit() or int(opcion) > len(ALGORITMOS) + 1:
            print("Opcion no valida")
            continue

        lista = leer_lista()
        opcion = int(opcion)

        if opcion == len(ALGORITMOS) + 1:
            for clase in ALGORITMOS:
                algoritmo = clase()
                resultado = algoritmo.ordenar(lista)
                print(f"{algoritmo.nombre:<12}: {resultado} Comparaciones: {algoritmo.comparaciones}\n")
        else:
            algoritmo = ALGORITMOS[opcion - 1]
            resultado = algoritmo.ordenar(lista)
            print(f"\n{algoritmo.nombre:<12}: {resultado}")
            print(f"{"Comparaciones":<12} {algoritmo.comparaciones}")

if __name__ == "__main__":
    main()

    ''' Colores en Python para el sistema en comandos, simbolo del sistema'''