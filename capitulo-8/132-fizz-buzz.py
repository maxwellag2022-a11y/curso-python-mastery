#famoso fizz buzz
#nos imprima todos los numeros hasta donde el usuario desee ingresar
#imrpima todos los numeros en la lista
#los multiplos de 3 que imrpima fizz
#los multiplos de 5 que imrpima buzz
#los multiplos de ambos que imprima fizz buzz

n = int(input("Ingrese hasta que digito desee imprimir: "))
for i in range(1,n+1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
