filas = 3
columnas = 3

matriz = []
for f in range(filas):
    fila = []
    for c in range(columnas):
        fila.append(0) 
    matriz.append(fila)

print("Actividad 04 - Matriz Bidimensional PYTHON")

for f in range(filas):
    for c in range(columnas):
        matriz[f][c] = int(input(f"Ingrese el valor para la posición [{f}][{c}]: "))

print("\nLos valores finales son:")
for f in range(filas):
    for c in range(columnas):
        print(matriz[f][c], end=" ")
    print()  