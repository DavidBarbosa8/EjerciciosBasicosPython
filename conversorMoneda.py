import requests
def convertirTasadeCambio(pesosColombianos,tasaCambio): #Se define la funcion con "def" se colocan los parametros y se colocan :
    dolares = pesosColombianos/tasaCambio
    return dolares

def retornarTasaCambio():

    URL = "https://api.exchangerate-api.com/v4/latest/USD"
    response = requests.get(URL)
    data = response.json()
    return data ["rates"]["COP"]


pesosColombianos = float(input ("Ingrese la cantidad de pesos colombianos: "))
#tasaCambio = float(input ("Ingrese la tasa de cambio "))
dolares = convertirTasadeCambio(pesosColombianos, retornarTasaCambio())
retornarTasaCambio()
print(f"{pesosColombianos} pesos colombianos son {dolares:2f} dolares")


