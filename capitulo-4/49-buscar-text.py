email = "usuario@academiafibonacci.com.gt"

print(email.find("@"))
print(email.find("xyz"))

print(email.index("@"))

arroba = email.find("@")
dominio = email[arroba + 1:]
Dominio = email[arroba:]
print(dominio)
print(Dominio)