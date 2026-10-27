"""Crea una clase Producto con nombre, precio y stock, y un metodo que calcule el valor del stock."""

class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def calcular_valor_stock(self):
        return self.precio * self.stock


def main():
    producto = Producto("Teclado Mecánico", 49.99, 15)
    print(f"Producto: {producto.nombre}")
    print(f"Precio: {producto.precio:.2f} €")
    print(f"Stock: {producto.stock} unidades")
    print(f"Valor total del stock: {producto.calcular_valor_stock():.2f} €")


if __name__ == "__main__":
    main()
