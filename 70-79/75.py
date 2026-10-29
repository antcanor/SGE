"""Crea una clase Pedido con líneas y un metodo total() que sume precio por cantidad."""
class LineaPedido:
    def __init__(self, producto: str, cantidad: int, precio_unitario: float):
        self.producto = producto
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario

    def subtotal(self) -> float:
        return self.cantidad * self.precio_unitario


class Pedido:
    def __init__(self):
        self.lineas = []

    def agregar_linea(self, producto: str, cantidad: int, precio_unitario: float):
        nueva_linea = LineaPedido(producto, cantidad, precio_unitario)
        self.lineas.append(nueva_linea)

    def total(self) -> float:
        return sum(linea.subtotal() for linea in self.lineas)

    def mostrar_resumen(self):
        for linea in self.lineas:
            print(f"- {linea.producto} x{linea.cantidad}: {linea.subtotal():,.2f}€")
        print("-" * 27)
        print(f"TOTAL: {self.total():,.2f}€\n")

def main():
    mi_pedido = Pedido()

    mi_pedido.agregar_linea("Teclado Mecánico", cantidad=2, precio_unitario=75.00)
    mi_pedido.agregar_linea("Ratón Óptico", cantidad=1, precio_unitario=22.50)
    mi_pedido.agregar_linea("Alfombrilla Gaming", cantidad=3, precio_unitario=15.00)

    mi_pedido.mostrar_resumen()

if __name__ == "__main__":
    main()
