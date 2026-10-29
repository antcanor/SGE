"""Define una excepción StockInsuficiente y úsala cuando una venta supere el stock."""

class StockInsuficiente(Exception):
    """Excepción lanzada cuando la cantidad solicitada supera las existencias disponibles."""
    pass


def vender_producto(producto, cantidad):
    """Realiza una venta descontando stock o lanza StockInsuficiente si no hay existencias."""
    if cantidad > producto.get("stock"):
        raise StockInsuficiente(
            f"No hay suficiente stock para '{producto['nombre']}'. "
            f"Disponible: {producto['stock']}, Solicitado: {cantidad}."
        )
    producto["stock"] -= cantidad
    return producto["stock"]


def main():
    articulo = {"nombre": "Tarjeta Gráfica RTX", "stock": 5}

    print(f"Producto: {articulo['nombre']} | Stock inicial: {articulo['stock']}")

    # Venta válida (3 unidades)
    try:
        nuevo_stock = vender_producto(articulo, 3)
        print(f"Venta realizada correctamente. Stock restante: {nuevo_stock}")
    except StockInsuficiente as error:
        print(f"Error en la venta: {error}")

    # Venta que supera el stock (se solicitan 4 pero solo quedan 2)
    try:
        nuevo_stock = vender_producto(articulo, 4)
        print(f"Venta realizada correctamente. Stock restante: {nuevo_stock}")
    except StockInsuficiente as error:
        print(f"Error capturado: {error}")


if __name__ == "__main__":
    main()
