"""Descuenta unidades del stock solo si hay suficientes existencias."""

def descontar_stock(producto, cantidad):
    """
    Descuenta unidades del stock del producto si hay suficientes existencias.
    Retorna True si la operación fue exitosa, o False si no había existencias suficientes.
    """
    if cantidad <= 0:
        return False

    if producto.get("stock") >= cantidad:
        producto["stock"] -= cantidad
        return True
    return False


def main():
    producto = {"codigo": "P01", "nombre": "Disco SSD 1TB", "stock": 10}

    print(f"Stock inicial de '{producto['nombre']}': {producto['stock']} unidades")

    # Intento 1: Venta válida de 4 unidades
    cantidad_venta = 4
    if descontar_stock(producto, cantidad_venta):
        print(f"Venta de {cantidad_venta} unidades realizada. Stock restante: {producto['stock']}")
    else:
        print(f"No hay suficientes existencias para vender {cantidad_venta} unidades.")

    # Intento 2: Venta inválida de 8 unidades (solo quedan 6)
    cantidad_venta = 8
    if descontar_stock(producto, cantidad_venta):
        print(f"Venta de {cantidad_venta} unidades realizada. Stock restante: {producto['stock']}")
    else:
        print(f"No hay suficientes existencias para vender {cantidad_venta} unidades (Stock actual: {producto['stock']}).")

    print(f"Stock final de '{producto['nombre']}': {producto['stock']} unidades")


if __name__ == "__main__":
    main()
