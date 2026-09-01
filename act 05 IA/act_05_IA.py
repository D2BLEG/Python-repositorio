def imprimir_pila(mensaje: str, pila: list[str]) -> None:
    """Función auxiliar para mostrar la pila de forma visual y limpia."""
    print(mensaje)
    # join() une todos los elementos con coma sin usar un bucle 'for' manual
    print(", ".join(pila))
    print("\n")

def push_aves(pila: list[str]) -> None:
    # extend() permite agregar múltiples elementos de una sola vez
    pila.extend(["Cotorro", "Quetzal", "Perico"])
    imprimir_pila("Los valores del vector (Pila) son:", pila)

def pop_aves(pila: list[str]) -> None:
    if pila:
        pila.pop()
    imprimir_pila("Los valores finales del vector (Pila) son:", pila)

def main() -> None:
    print("Actividad 05 - Memoria Dinámica - Vector de nombres (String/POP/PUSH)\n")
    
    # Creamos la lista base
    pila_aves = ["Loro gris", "Paloma diamante", "Guacamaya"]

    # Como las listas en Python son mutables, las funciones la modifican directamente
    push_aves(pila_aves)
    pop_aves(pila_aves)

if __name__ == "__main__":
    main()
