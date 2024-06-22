# La serie Fibonacci es una sucesión de números enteros, comenzando en 0 y 1, 
# cada uno se calcula sumando los dos anteriores. Escribir un programa que calcule los 50 primeros números de la serie Fibonacci.

# a + b = c
# 0 + 1 = 1, 1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8


a = 0
b = 1
c = 0
for i in range(10):
    c = a + b
    a = b
    b = c

    print (c)
