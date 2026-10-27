"""Crea un diccionario de productos y precios y calcula el valor total de comprar una unidad de cada uno."""

def calcular_total(precios):
    return sum(precios.values())


def main():
    # Diccionario de productos y precios unitarios
    catalogo = {
        "Manzana": 1.20,
        "Pan": 0.85,
        "Leche": 1.50,
        "Huevos": 2.30,
        "Café": 4.50
    }

    print("Catálogo de productos y precios:")
    for producto, precio in catalogo.items():
        print(f"- {producto}: {precio:.2f} €")

    total = calcular_total(catalogo)
    print(f"\nTotal al comprar una unidad de cada uno: {total:.2f} €")


if __name__ == "__main__":
    main()
