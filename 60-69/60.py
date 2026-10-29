"""Cuenta cuántos pedidos hay en cada estado."""

def contar_pedidos_por_estado(pedidos):
    """Devuelve un diccionario con el recuento de pedidos por cada estado."""
    conteo = {}
    for pedido in pedidos:
        estado = pedido.get("estado")
        conteo[estado] = conteo.get(estado, 0) + 1
    return conteo


def main():
    pedidos = [
        {"id": 1, "cliente": "Juan", "estado": "pendiente"},
        {"id": 2, "cliente": "María", "estado": "enviado"},
        {"id": 3, "cliente": "Carlos", "estado": "entregado"},
        {"id": 4, "cliente": "Lucía", "estado": "pendiente"},
        {"id": 5, "cliente": "Pedro", "estado": "cancelado"},
        {"id": 6, "cliente": "Ana", "estado": "enviado"},
        {"id": 7, "cliente": "David", "estado": "entregado"},
        {"id": 8, "cliente": "Elena", "estado": "entregado"},
    ]

    resultado = contar_pedidos_por_estado(pedidos)

    print("Recuento de pedidos por estado:")
    for estado, cantidad in resultado.items():
        print(f"- {estado.capitalize()}: {cantidad} pedido(s)")


if __name__ == "__main__":
    main()
