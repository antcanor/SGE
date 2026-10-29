"""Ordena productos por precio ascendente."""

def ordenar_por_precio(productos):
    """Devuelve una nueva lista de productos ordenada por precio de forma ascendente."""
    return sorted(productos, key=lambda producto: producto["precio"])


def main():
    productos = [
        {"nombre": "Monitor 27\"", "precio": 199.99},
        {"nombre": "Teclado Mecánico", "precio": 49.95},
        {"nombre": "Alfombrilla XL", "precio": 12.50},
        {"nombre": "Ratón Inalámbrico", "precio": 24.99},
        {"nombre": "Auriculares Gaming", "precio": 79.90},
    ]

    print("Productos ordenados por precio ascendente:")
    productos_ordenados = ordenar_por_precio(productos)
    for p in productos_ordenados:
        print(f"- {p['nombre']}: {p['precio']:.2f} €")


if __name__ == "__main__":
    main()
