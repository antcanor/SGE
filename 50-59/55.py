"""Amplía la clase Producto para rechazar precios negativos."""

class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio  # Se valida a través del setter
        self.stock = stock

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, valor):
        if valor < 0:
            raise ValueError("El precio no puede ser negativo.")
        self._precio = valor

    def calcular_valor_stock(self):
        return self.precio * self.stock


def main():
    # Instanciación correcta
    producto = Producto("Ratón Inalámbrico", 25.50, 20)
    print(f"Producto creado: {producto.nombre}, Precio: {producto.precio:.2f} €, Stock: {producto.stock}")
    print(f"Valor del stock: {producto.calcular_valor_stock():.2f} €")

    # Prueba de validación al instanciar con precio negativo
    print("\nIntentando crear producto con precio negativo (-150 €):")
    try:
        producto_invalido = Producto("Monitor", -150.0, 5)
    except ValueError as e:
        print(f"Error capturado: {e}")

    # Prueba de validación al asignar precio negativo a producto existente
    print("\nIntentando asignar precio negativo (-10 €) a un producto existente:")
    try:
        producto.precio = -10.0
    except ValueError as e:
        print(f"Error capturado: {e}")


if __name__ == "__main__":
    main()
