import pandas as pd

estudiantes = {"Nombres": ["Juan", "Maria", "Pedro","Jose","Carlos"], "Edad": [20, 22, 21, 19, 18], "Calificaciones": [8, 9, 10, 7, 6]}

estudiantesDF = pd.DataFrame(estudiantes)

print (estudiantesDF)