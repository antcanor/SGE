"""Representa pedidos con un campo cliente_id y agrupa sus importes por cliente."""

def agrupar_importes_cliente(lista):
    totales_cliente = {}
    for pedido in lista:
        cliente = pedido["cliente_id"]
        importe = pedido["importe"]
        if cliente not in totales_cliente:
            totales_cliente[cliente] = 0.0
        totales_cliente[cliente] += importe
    return totales_cliente

def main():
    pedidos = [
        {"pedido_id": 1, "cliente_id": "C100", "importe": 45.50},
        {"pedido_id": 2, "cliente_id": "C200", "importe": 120.00},
        {"pedido_id": 3, "cliente_id": "C100", "importe": 15.25},
        {"pedido_id": 4, "cliente_id": "C300", "importe": 89.99},
        {"pedido_id": 5, "cliente_id": "C200", "importe": 35.00},
    ]

    resultado = agrupar_importes_cliente(pedidos)
    print(resultado)


if __name__ == "__main__":
    main()
