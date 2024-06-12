num1 = float(input("Ingrese el numero a evaluar \n"))
num2 = 2
resultado = num1 % num2

if(resultado > 0):
    print ("El numero es impar")
elif (resultado < 0):
    print ("EL numero es impar")
else:
    print(f"El numero {num1} es par")
