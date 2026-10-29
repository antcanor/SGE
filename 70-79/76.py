"""Crea una clase Pedido con estado inicial 'borrador' y
un metodo confirmar() que solo permita pasar de borrador a confirmado."""

class Pedido:
    def __init__(self):
        self.estado = "borrador"

    def confirmar(self):
        if self.estado == "borrador":
            self.estado = "confirmado"
            print(f" El Pedido se ha sido CONFIRMADO.")
        else:
            print(f"Error: No se puede confirmar. El pedido ya está en estado '{self.estado}'.")


def main():
    pedido_1 = Pedido()
    print(f"Estado inicial: {pedido_1.estado}")
    pedido_1.confirmar()
    print(f"Estado actual: {pedido_1.estado}")
    pedido_1.confirmar()

    pedido_2 = Pedido()
    pedido_2.estado = "cancelado"
    print(f"Estado inicial: {pedido_2.estado}")

    pedido_2.confirmar()



if __name__ == "__main__":
    main()
