"""Representa un pedido como una lista de líneas, cada una con precio y cantidad, y calcula el total."""

def calcular_total(pedido):
    """Calcula el importe total de un pedido a partir de su lista de líneas."""
    total = 0.0
    for linea in pedido:
        total += linea["precio"] * linea["cantidad"]
    return total


def main():
    # Representación de un pedido como una lista de líneas
    pedido = [
        {"producto": "Teclado Mecánico", "precio": 45.0, "cantidad": 2},
        {"producto": "Ratón Óptico", "precio": 18.5, "cantidad": 3},
        {"producto": "Alfombrilla", "precio": 9.99, "cantidad": 1},
    ]

    print("Detalle de las líneas del pedido:")
    for linea in pedido:
        subtotal = linea["precio"] * linea["cantidad"]
        print(f"- {linea['producto']}: {linea['cantidad']} x {linea['precio']:.2f} € = {subtotal:.2f} €")

    total = calcular_total(pedido)
    print(f"\nTotal del pedido: {total:.2f} €")


if __name__ == "__main__":
    main()
