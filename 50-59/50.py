"""Crea una función que reciba una lista de precios y devuelva el precio máximo, o None si está vacía."""

def ejercicio(lista):
    if len(lista)==0:
        return None
    return max(lista)


def main():
    print(ejercicio((1.84,55.51,65.6,15.8,99.25,231.2)))

if __name__ == "__main__":
    main()
