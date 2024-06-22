"""
Debemos generar un programa que sume todos los numeros pares del 1 al 100
"""
numPares = []

for i in range (1,101):
    if i % 2 == 0:
        numPares.append(i) # .append significa que estamos adicionando valores a la lista seleccionada

print(numPares)
print (sum(numPares))


