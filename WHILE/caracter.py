#Contador de caracteres dentro de una cadena

cadena = input("Introduce un texto cualquiera \n")
caracter = input("Ingresa el caracter que quieres contar \n")
c = 0

for i in cadena:
    if i == caracter:
        c += 1

print(c)
