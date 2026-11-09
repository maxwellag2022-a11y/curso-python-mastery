#numero = 8
#if numero > 0:
 #   print("positivo")
#elif numero < 0:
 #   print("negativo")
#else:
 #   print("CERO")


#opcion = input("Ingrese la opcion (1,2,3,4): ")

#match opcion:
    #case "1":
     #   print("Listar productos")
    #case "2":
#        print("Crear producto")
 #   case "3":
  #      print("Editar producto")
#    case "4":
 #       print("Salir")
#    case _:
 #       print("Opcion invalida")

opcion = input("Ingrese la opcion: ")

if opcion == "1":
    print("Listar productos")
elif opcion == "2":
    print("Crear productos")
elif opcion == "3":
    print("Editar productos")
elif opcion == "4":
    print("Salir")
else:
    print("Opcion invalida")