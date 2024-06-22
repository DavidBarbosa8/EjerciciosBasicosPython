"""
Multiplicación: Hacer un programa que solicite al usuario números enteros siempre y cuando sean menores de 10 
e imprima la multiplicación de cada uno de los números digitados(3*5*6*3..). Cuando el usuario digite un número mayor 
de 10 imprima la multiplicación que lleva hasta el momento

"""
numeros = 1
memoriaNumeros = []
resultado = 1

while numeros > 0 and numeros <= 10:
         
        numeros = int(input("Ingresa numeros enteros entre 1 y 10 para imprimir la multiplicación \n"))
        memoriaNumeros.append(numeros)

        if (numeros > 10):
                print(memoriaNumeros)
                memoriaNumeros.pop()
        elif (numeros == 0):
                memoriaNumeros.pop()

for i in memoriaNumeros:

                resultado *= i 

print (f"La multiplicacion de {memoriaNumeros} es:  {resultado}")


        

        
  














# while numeros <= 10:

#     numeros = int(input("Ingresa numeros entre 1 y 10 para imprimir la multiplicación \n"))   
#     memoriaNumeros += numeros

# print(f"La multiplicacion de tus numeros es: {memoriaNumeros}")