def pop_arreglos_aves(vector_pop):
    vector_pop.pop()
    print("Los valores finales del vector (Pila) son: ")
    for i in range(len(vector_pop)):
        print(vector_pop[i], end=", ")
    print("\n")

def push_arreglos_aves(vector_push):
    vector_push.append("Cotorro")
    vector_push.append("Quetzal")
    vector_push.append("Perico")
    print("Los valores del vector (Pila) son: ")
    for i in range(len(vector_push)):
        print(vector_push[i], end=", ")
    print("\n")
    return vector_push

def main():
    print("Actividad 05 - Memoria Dinamica - Vector de nombres (String/POP/PUSH)")
    aves = ["Loro gris", "Paloma diamante", "Guacamaya"]
    nuevas_aves = []
    nuevas_aves = push_arreglos_aves(aves)
    pop_arreglos_aves(nuevas_aves)

if __name__ == "__main__":
    main()