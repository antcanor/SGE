"""Crea una función que elimine referencias duplicadas de una lista sin cambiar el orden de la primera aparición."""

def eliminar_duplicados_orden(lista):
    resultado = []
    for item in lista:
        if item not in resultado:
            resultado.append(item)
    return resultado


def main():
    referencias = [
        "REF-01",
        "REF-02",
        "REF-01",
        "REF-03",
        "REF-02",
        "REF-04",
        "REF-01",
        "REF-05"
    ]

    print("Lista original con duplicados:")
    print(referencias)

    sin_duplicados = eliminar_duplicados_orden(referencias)

    print("\nLista sin duplicados (manteniendo el orden de aparición):")
    print(sin_duplicados)


if __name__ == "__main__":
    main()
