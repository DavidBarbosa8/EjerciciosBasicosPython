"""
Perfiles de hierro: Una planta que fabrica perfiles de hierro posee un lote de n piezas.
Diseñar un programa que pida ingresar por teclado la cantidad de piezas a procesar e ingrese 
la longitud de cada perfil, sabiendo que la pieza cuya longitud este comprendida entre 1.20 y 1.30 son aptas. 
Imprimir la cantidad de piezas del lote que son aptas
"""

cantPiezas = int(input("Ingrese la cantidad de piezas a procesar: "))
contador = 1
# for i in range(cantPiezas):
#     longPieza = float(input("Ingrese la longitud de la pieza: "))
#     if longPieza >= 1.2 and longPieza <= 1.3:
#         print("Pieza apta")
#     else:
#         print("Pieza no apta")

while contador <= cantPiezas:

    longPerfil = float(input(f"Ingrese la longitud de la pieza # {contador}: "))
    if longPerfil >= 1.20 and longPerfil <= 1.30:
        print (f"Pieza apta, ingrese la siguiente pieza ")
        contador += 1
    else:
        print (f"Pieza no apta continue ingresando la pieza # {contador}")
        