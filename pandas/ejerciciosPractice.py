import pandas as pd

# 2- Filtra los datos para obtener las filas donde la Edad sea mayor a 30 y el Salario sea menor a 35000.
# 3- Filtra los datos para obtener las filas donde la Ciudad sea 'Madrid'.
# 4-obtener las filas donde la Ciudad sea 'Madrid' y el Salario sea mayor a 30000.

data = { 'Nombre': ['Ana', 'Luis', 'Carlos', 'Marta', 'Pedro'], 'Edad': [23, 45, 35, 25, 30], 'Ciudad': ['Madrid', 'Barcelona', 'Madrid', 'Valencia', 'Sevilla'], 'Salario': [30000, 40000, 35000, 32000, 28000] }
df = pd.DataFrame(data)

# 2- Filtra los datos para obtener las filas donde la Edad sea mayor a 30 y el Salario sea menor a 35000.

print (df[(df["Edad"] > 30 ) & (df["Salario"] < 35000)])

# 3- Filtra los datos para obtener las filas donde la Ciudad sea 'Madrid'.

print (df[df["Ciudad"] == "Madrid"])

# 4-obtener las filas donde la Ciudad sea 'Madrid' y el Salario sea mayor a 30000.

print (df[(df["Ciudad"] == "Madrid") & (df["Salario"] > 30000)])

