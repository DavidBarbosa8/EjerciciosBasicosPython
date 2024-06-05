# Validación rango: Solicita al usuario un número y comprueba si el número está en el rango de 10 a 20(inclusive) e imprime el resultado

usuario = float(input("Ingresa un numero entre 10 y 20 \n"))

print (f"Tu numero es {usuario}")

if(usuario < 10 ):
    print ("Tu numero no esta en el rango solicitado")
elif(usuario > 20):
     print ("Tu numero no esta en el rango solicitado")
else:
    print ("Tu eleccion es correcta")