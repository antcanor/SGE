"""Diseña una clase Inventario con métodos para añadir productos,
consultar stock y registrar una salida con validación."""

class Inventario:
    def __init__(self):
        self.productos = {}

    def anadir_producto(self, codigo, nombre, stock=0):
        self.productos[codigo] = {
            "nombre": nombre,
            "stock": max(0, stock)
        }

    def consultar_stock(self, codigo):
        if codigo in self.productos:
            return self.productos[codigo]["stock"]
        return None

    def registrar_salida(self, codigo, cantidad):
        if codigo not in self.productos:
            raise ValueError(f"El producto con código '{codigo}' no existe.")
        if cantidad <= 0:
            raise ValueError("La cantidad de salida debe ser mayor que cero.")
        if self.productos[codigo]["stock"] < cantidad:
            raise ValueError(
                f"Stock insuficiente para '{self.productos[codigo]['nombre']}'. "
                f"Disponible: {self.productos[codigo]['stock']}, Solicitado: {cantidad}."
            )

        self.productos[codigo]["stock"] -= cantidad
        return self.productos[codigo]["stock"]


def main():
    inv = Inventario()

    # 1. Añadir productos
    inv.anadir_producto("P01", "Teclado Mecánico", stock=10)
    inv.anadir_producto("P02", "Ratón Óptico", stock=5)

    print("--- Stock inicial ---")
    print(f"Stock P01: {inv.consultar_stock('P01')} uds")
    print(f"Stock P02: {inv.consultar_stock('P02')} uds")

    # 2. Registrar salida válida
    print("\n--- Salida válida de 4 unidades de P01 ---")
    nuevo_stock = inv.registrar_salida("P01", 4)
    print(f"Salida realizada. Stock restante de P01: {nuevo_stock} uds")

    # 3. Registrar salida con cantidad excesiva (error)
    print("\n--- Intentando salida de 10 unidades de P02 (solo hay 5) ---")
    try:
        inv.registrar_salida("P02", 10)
    except ValueError as e:
        print(f"Error capturado: {e}")

    # 4. Registrar salida de producto inexistente (error)
    print("\n--- Intentando salida de producto inexistente (P99) ---")
    try:
        inv.registrar_salida("P99", 1)
    except ValueError as e:
        print(f"Error capturado: {e}")


if __name__ == "__main__":
    main()
