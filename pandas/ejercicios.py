import pandas as pd

# se agrega index con el fin de darle indice a cada valor de la lista

list1 = pd.Series(["Lavadora","Nevera","TV","Licuadora"], index = [1,22,3,6])

print (list1)

# se crea un diccionario

dic = {1: "TV", 2: "Nevera", 3: "Lavadora", 4: "Licuadora"}
dict = pd.Series (dic)

print (dict)


# creamos un dataframe

dict2 = {"Jugador": ["Messi","Cristiano","Ronaldo","Neymar","Mbappe"],"Equipo":["Barcelona","Juventus","Real Madrid","Paris Saint Germain","PSG"],"Posicion":["Delantero","Medio","Defensa","Delantero","Delantero"]}
dataF = pd.DataFrame(dict2)

print (dataF)

# seleccionar valores especificos del data frame

print (dataF [0:4]) # siempre toma el valor anterior como con las matrices

# se pueden agregar indices

jugadores = pd.DataFrame (dict2, index = [1,3,5,6,7])

print (jugadores)

