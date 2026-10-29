"""Escribe una función que busque un producto por su código y devuelva el diccionario o None."""

def buscar_por_codigo(productos, codigo):
    """Busca un producto por su código identificador. Retorna el diccionario o None."""
    for producto in productos:
        if producto.get("codigo") == codigo:
            return producto
    return None


def main():
    catalogo = [
        {"codigo": "A101", "nombre": "Teclado USB", "precio": 19.99},
        {"codigo": "B202", "nombre": "Ratón Óptico", "precio": 14.50},
        {"codigo": "C303", "nombre": "Webcam HD", "precio": 39.00},
        {"codigo": "D404", "nombre": "Micrófono", "precio": 29.95},
    ]

    codigo_a_buscar = "B202"
    resultado = buscar_por_codigo(catalogo, codigo_a_buscar)
    print(f"Búsqueda de código '{codigo_a_buscar}': {resultado}")

    # Búsqueda de un código inexistente
    codigo_inexistente = "Z999"
    resultado_fallido = buscar_por_codigo(catalogo, codigo_inexistente)
    print(f"Búsqueda de código '{codigo_inexistente}': {resultado_fallido}")


if __name__ == "__main__":
    main()
