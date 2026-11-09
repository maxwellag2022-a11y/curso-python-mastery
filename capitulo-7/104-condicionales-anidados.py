edad = int(input("Digite su edad: "))

if edad >= 18:
    pais = input("PAIS (GT/US/EU)").upper().strip()
    if pais == "GT":
        print("Eres elegible para votar en Guatemala")
    elif pais == "USA":
        print("Eres elegible para votar en Estados Unidos")
    elif pais == "EU":
        print("Eres elegible para votar en la Union Europea")
    else:
        print("Revisa las leyes de tu pais")
else:
    print("Aun no puedes votar")