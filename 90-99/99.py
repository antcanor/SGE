"""A partir de ventas con vendedor e importe, calcula una comisión del 3 % por vendedor."""

def calcular_comisiones(ventas, porcentaje_comision=0.03):
    ventas_por_vendedor = {}
    for venta in ventas:
        vendedor = venta["vendedor"]
        ventas_por_vendedor[vendedor] = ventas_por_vendedor.get(vendedor, 0.0) + venta["importe"]

    return {
        vendedor: round(total * porcentaje_comision, 2)
        for vendedor, total in ventas_por_vendedor.items()
    }


def main():
    ventas = [
        {"vendedor": "Ana", "importe": 1000.0},
        {"vendedor": "Carlos", "importe": 500.0},
        {"vendedor": "Ana", "importe": 800.0},
        {"vendedor": "Lucía", "importe": 1250.0},
        {"vendedor": "Carlos", "importe": 450.0},
        {"vendedor": "Lucía", "importe": 350.0},
    ]

    print("--- Registro de ventas ---")
    for v in ventas:
        print(f"Vendedor: {v['vendedor']} | Importe: {v['importe']:7.2f} €")

    comisiones = calcular_comisiones(ventas, porcentaje_comision=0.03)

    print("\n--- Comisiones del 3 % por vendedor ---")
    for vendedor, comision in comisiones.items():
        print(f"- {vendedor}: {comision:.2f} €")


if __name__ == "__main__":
    main()
