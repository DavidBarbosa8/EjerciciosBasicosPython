#Imprimir la tabla de multiplicar de un numero:
#Pide al usuario un numero y lo multiplica por todos los numeros del 1 al 10


numero = int(input("Ingresa un numero \n"))

for i in range(1,11):
    print(f"{numero} x {i} = {numero*i}")

    

