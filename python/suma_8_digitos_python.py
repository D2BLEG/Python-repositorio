# variables 
limite = 8
lista = []

for i in range(limite):
    dato = int(input("ingresa un numero a sumar: "))
    lista.append(dato)

print("sumatoria de los 8 digitos:", sum(lista))
