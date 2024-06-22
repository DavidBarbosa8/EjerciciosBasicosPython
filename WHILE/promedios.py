#Leer calificaciones del estudiante y mostrar promedios

notas = int(input("Cuantas notas vas a ingresar? \n")) #Captura los datos del usuario
contador = 1
promedio = 0
sumaNotas = 0

while contador <= notas:

    notasTotales = float(input (f"Ingresa la nota {contador} \n"))

    if notasTotales < 0 or notasTotales > 5:
        print("Error, la nota tiene que ser entre 0 y 5")
        notasTotales = float(input (f"Ingresa la nota {contador} \n"))

   
    sumaNotas += notasTotales
    contador += 1
        
promedio = sumaNotas / notas

print(f"Tu promedio es {promedio:.2f} con las notas ingresadas")

   




