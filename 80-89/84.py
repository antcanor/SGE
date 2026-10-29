"""Ordena pedidos cuya fecha está en formato AAAA-MM-DD."""

def ordenar_pedidos_por_fecha(lista_pedidos, descendente= False):
    return sorted(lista_pedidos, key=lambda pedido: pedido["fecha"], reverse=descendente)


def main():
    pedidos = [
        {"pedido_id": 1, "fecha": "2026-03-15", "importe": 45.50},
        {"pedido_id": 2, "fecha": "2026-01-10", "importe": 120.00},
        {"pedido_id": 3, "fecha": "2026-10-29", "importe": 15.25},
        {"pedido_id": 4, "fecha": "2026-05-22", "importe": 89.99},
    ]

    pedidos_ordenados = ordenar_pedidos_por_fecha(pedidos)
    print("Ordenados cronológicamente:")
    for p in pedidos_ordenados:
        print(p)

    print("\nOrdenados de más recientes a más antiguos:")
    pedidos_recientes = ordenar_pedidos_por_fecha(pedidos, descendente=True)
    for p in pedidos_recientes:
        print(p)


if __name__ == "__main__":
    main()
