import pandas as pd

libros = pd.read_csv("./bestsellers-with-categories-Restore.csv", sep = ",") # con sep se cambia el identificador de columnas dentro del archivo para que tome el identificador correcto, por defecto toma ","

# print (libros)

# print (libros[0:7]) # puedo seleccionar cualquier parte del dataframe y mostrarlo

# print (libros[["Name","Author"]]) # puedo seleccionar columnas especificas

# print (libros.loc[0:5, ["Name","Price"]]) # puedo seleccionar los datos que yo quiera de las columnas

# print (libros.loc[:, ["Author"]] == "Stephen King") # puedo seleccionar cuantas veces se repite el dato que yo quiera

print (libros[(libros["Author"] == "Stephen King") & (libros["User Rating"]>4)]) # puedo anidar condiciones en los filtros que genero
# Un dato importante es que debemos usar con la funcion print un ([]) <----- siempre y dentro de esa estructura anidar las condiciones que queramos separadas por parentesis () entre ellas
 

#print(libros[(libros['User Rating'] > 4.6) & (libros['Gender'] == 'Fiction')])

# data = { 'Nombre': ['Ana', 'Luis', 'Carlos', 'Marta', 'Pedro'], 'Edad': [23, 45, 35, 25, 30], 'Ciudad': ['Madrid', 'Barcelona', 'Madrid', 'Valencia', 'Sevilla'], 'Salario': [30000, 40000, 35000, 32000, 28000] }
# df = pd.DataFrame(data)

# print (df[df["Edad"] > 30])




