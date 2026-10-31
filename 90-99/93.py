"""Crea una función que valide líneas de pedido, calcule subtotales y devuelva el total. Rechaza cantidades no positivas y precios negativos."""

def procesar_lineas_pedido(lineas):

    total = 0.0
    for linea in lineas:
        if linea["cantidad"] <= 0:
            raise ValueError("La cantidad debe ser mayor que cero.")
        if linea["precio"] < 0:
            raise ValueError("El precio no puede ser negativo.")

        linea["subtotal"] = round(linea["precio"] * linea["cantidad"], 2)
        total += linea["subtotal"]

    return round(total, 2)


def main():
    pedido = [
        {"producto": "Teclado", "precio": 49.99, "cantidad": 2},
        {"producto": "Ratón", "precio": 19.50, "cantidad": 3},
        {"producto": "Alfombrilla", "precio": 10.00, "cantidad": 1},
    ]

    print("--- Pedido antes de procesar ---")
    for l in pedido:
        print(l)

    total = procesar_lineas_pedido(pedido)

    print("\n--- Pedido después de calcular subtotales ---")
    for l in pedido:
        print(f"- {l['producto']}: {l['cantidad']} x {l['precio']} € = {l['subtotal']} €")
    print(f"\nTotal: {total:.2f} €")

    # Prueba de validación
    print("\n--- Probando cantidad inválida (0) ---")
    try:
        procesar_lineas_pedido([{"producto": "Monitor", "precio": 100, "cantidad": 0}])
    except ValueError as e:
        print(f"Error capturado: {e}")


if __name__ == "__main__":
    main()
