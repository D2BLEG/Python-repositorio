numeroFilas = 3
numeroColumnas = 3

def impresion_arreglo(arr_dos):
    print("Los valores finales de la lista bidimensional son: \n")
    for i in range(numeroFilas):
        for j in range(numeroColumnas):
            print(arr_dos[i][j], end=" ")
        print("\n")

def captura_valores_matriz(a):
    for f in range(numeroFilas):
        for c in range(numeroColumnas):
            a[f][c] = int(input("Ingrese los valores de la posición [" + str(f) + "][" + str(c) + "] :\n"))

def main():
    arreglo_bidimensional = [[0] * numeroColumnas for _ in range(numeroFilas)]
    print("Actividad 04 - Matriz Bidimensional PYTHON- (Matriz de MxN) ")
    captura_valores_matriz(arreglo_bidimensional)
    impresion_arreglo(arreglo_bidimensional)

if __name__ == "__main__":
    main()
