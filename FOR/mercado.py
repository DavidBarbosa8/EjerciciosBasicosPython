totalProductos = int(input("Cuantos productos hay en el carrito: ")) #Se recolecta la cantidad de productos que lleva el cliente
total = 0
for productos in range(totalProductos):  #Se hace un for para que itere la cantidad de veces que el cliente indique
    precio = float (input("Introduce el precio del producto: ")) #Se toma el precio de cada producto iterando la cantidad de veces que indique el cliente
    total += precio

print(f"El total de la compra es : ${total}")
