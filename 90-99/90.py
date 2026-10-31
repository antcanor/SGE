"""Agrupa importes por mes usando fechas AAAA-MM-DD."""

def agrupar_ventas_por_mes(ventas):
    ventas_por_mes = {}
    for venta in ventas:
        mes = venta["fecha"][:7]
        importe = venta["importe"]
        if mes not in ventas_por_mes:
            ventas_por_mes[mes] = 0.0
        ventas_por_mes[mes] = round(ventas_por_mes[mes] + importe, 2)
    return ventas_por_mes


def main():
    ventas = [
        {"id": 1, "fecha": "2026-01-15", "importe": 120.50},
        {"id": 2, "fecha": "2026-01-28", "importe": 45.00},
        {"id": 3, "fecha": "2026-02-04", "importe": 89.90},
        {"id": 4, "fecha": "2026-02-19", "importe": 210.00},
        {"id": 5, "fecha": "2026-03-02", "importe": 65.25},
        {"id": 6, "fecha": "2026-03-25", "importe": 150.75},
        {"id": 7, "fecha": "2026-03-30", "importe": 34.50},
    ]

    totales_mes = agrupar_ventas_por_mes(ventas)

    print("Total de ventas agrupadas por mes:")
    for mes, total in totales_mes.items():
        print(f"- {mes}: {total:.2f} €")


if __name__ == "__main__":
    main()
