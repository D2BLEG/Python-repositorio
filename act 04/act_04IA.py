def captura_valores_matriz(filas: int, columnas: int) -> list[list[int]]:
    """Crea y llena una matriz bidimensional con valores ingresados por el usuario."""
    matriz = []
    for f in range(filas):
        fila = []
        for c in range(columnas):
            val = int(input(f"Ingrese el valor de la posición [{f}][{c}]: "))
            fila.append(val)
        matriz.append(fila)
        print()  # Espaciado entre filas durante la captura
    return matriz


def impresion_arreglo(matriz: list[list[int]]) -> None:
    """Imprime los valores de la matriz en formato tabular."""
    print("Los valores finales de la lista bidimensional son:\n")
    for fila in matriz:
        for elemento in fila:
            print(f"{elemento}\t", end="")
        print()  # Salto de línea limpio al terminar cada fila


def main():
    filas = 3
    columnas = 3

    print("Actividad 04 - Matriz Bidimensional PYTHON (Matriz de MxN)\n")
    matriz = captura_valores_matriz(filas, columnas)
    impresion_arreglo(matriz)


if __name__ == "__main__":
    main()