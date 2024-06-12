#El usuario ingresa numeros, y una vez ingresa un numero negativo termina el programa

contador = -1
num = 0
while num >=0:
    num = float(input("Ingresa la cantidad de numeros que desees y luego escribe un numero negativo: "))
    contador += 1

print(f"Has escrito {contador} numeros antes de colocar el numero negativo")
    
