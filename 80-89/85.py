
def calcular_metricas_pedidos(lista_pedidos):
    total_pedidos = len(lista_pedidos)
    if total_pedidos == 0:
        return {"numero_pedidos": 0, "importe_total": 0.0, "ticket_medio": 0.0}
    importe_total = sum(pedido["importe"] for pedido in lista_pedidos)
    ticket_medio = round(importe_total / total_pedidos, 2)
    return {
        "numero_pedidos": total_pedidos,
        "importe_total": round(importe_total, 2),
        "ticket_medio": ticket_medio
    }

def main():
    pedidos = [
        {"pedido_id": 1, "fecha": "2026-03-15", "importe": 45.50},
        {"pedido_id": 2, "fecha": "2026-01-10", "importe": 120.00},
        {"pedido_id": 3, "fecha": "2026-10-29", "importe": 15.25},
        {"pedido_id": 4, "fecha": "2026-05-22", "importe": 89.99},
    ]

    resultado = calcular_metricas_pedidos(pedidos)
    print(resultado)

if __name__ == "__main__":
    main()
