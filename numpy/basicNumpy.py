import numpy as np

lista = [8,4,6,7,100] # array unidimensional

print (lista)

array = np.array([lista]) # Asi se denota un arreglo para la libreria numpy

print (array)

#matrices

matriz = [[1,2,3],[4,5,6],[7,8,9]] #arreglo

matriz = np.array(matriz)
print (matriz)

# tomar una serie de numeros con arange

arrNumeros = np.arange(10,51) #con esta funcion toma los numeros de 10 hasta 50
print (arrNumeros)

# tomar numeros ordenados en una cantidad de columnas y filas

matrizNumeros = np.arange(0,9).reshape(3,3) # arange denota el rango y .reshape denota la cantidad de columnas y filas
print (matrizNumeros)

# hacer una matriz de ceros

matrizCeros = np.zeros(9).reshape(3,3) #np.zeros crea una matriz de solos ceros dependiendo del reshape
print (matrizCeros)

#promedio de un array

arr = np.array([10,20,30,40,50,60,70,80,90,100])
print (arr.mean())

# suma de arrays

arr = np.array([10,20,30,40,50,60,70,80,90,100])
arr2 = np.array([1,2,3,4,5,6,7,8,9,10])
print (arr+arr2)

# array con 5 elementos

arr = np.array([1,2,3,4,5])

# suma de todos los elementos

print (arr.sum())

#matriz de 5 filas y 4 columnas con numeros aleatorios entre 1 y 10

matriz3 = np.random.randint(1,10, size = (5,4)) # se declara el tamaño de la matriz requerida dentro del mismo randint
print (matriz3)
print (np.max(matriz3))

# Acceder al elemento "9"del siguiente array

arrayx =np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])

print (arrayx[2,2])

# matriz 5 x 5 y se va a obtener el valor maximo de la matriz
matriz4 = np.random.randint(1,100, size = (5,5)) # asi se declara un rango de numeros (1,100) y de los cuales va a tomar al azar los numeros que necesite para formar una matriz 5x5
print (matriz4)
print (np.max(matriz4))




