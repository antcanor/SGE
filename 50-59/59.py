"""Agrupa una lista de productos por categoría en un diccionario."""

def agrupar_por_categoria(productos):
    """Agrupa productos por su categoría en un diccionario."""
    categorias = {}
    for producto in productos:
        cat = producto["categoria"]
        if cat not in categorias:
            categorias[cat] = []
        categorias[cat].append(producto["nombre"])
    return categorias


def main():
    productos = [
        {"nombre": "Manzana", "categoria": "Frutas"},
        {"nombre": "Plátano", "categoria": "Frutas"},
        {"nombre": "Leche", "categoria": "Lácteos"},
        {"nombre": "Queso", "categoria": "Lácteos"},
        {"nombre": "Yogur", "categoria": "Lácteos"},
        {"nombre": "Pan", "categoria": "Panadería"},
    ]

    agrupados = agrupar_por_categoria(productos)

    for categoria, items in agrupados.items():
        print(f"{categoria}: {', '.join(items)}")


if __name__ == "__main__":
    main()
