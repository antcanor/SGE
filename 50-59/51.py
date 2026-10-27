"""Crea un diccionario de productos y precios y calcula el valor total de comprar una unidad de cada uno."""
def ejercicio(diccionario):
    total = 0
    if len(diccionario) == 0:
        return total
    else:
        for producto in diccionario:
            total += diccionario[producto]

    return total
def main():
    diccionario_productos = {
        "Manzana": 1.20,
        "Pan": 0.85,
        "Leche": 1.50,
        "Huevos": 2.30,
        "Café": 4.50
    }
    print(ejercicio(diccionario_productos))

if __name__ == "__main__":
    main()
