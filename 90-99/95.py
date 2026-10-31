"""Genera un resumen con número de referencias, unidades totales y valor total del inventario."""

def generar_resumen_inventario(inventario):
    numero_referencias = len(inventario)
    unidades_totales = sum(p["stock"] for p in inventario)
    valor_total = sum(p["stock"] * p["precio"] for p in inventario)

    return {
        "numero_referencias": numero_referencias,
        "unidades_totales": unidades_totales,
        "valor_total": round(valor_total, 2)
    }


def main():
    inventario = [
        {"referencia": "REF-001", "nombre": "Teclado USB", "stock": 15, "precio": 25.00},
        {"referencia": "REF-002", "nombre": "Ratón Óptico", "stock": 30, "precio": 12.50},
        {"referencia": "REF-003", "nombre": "Monitor 24\"", "stock": 8, "precio": 140.00},
        {"referencia": "REF-004", "nombre": "Cable HDMI", "stock": 50, "precio": 4.50},
    ]

    print("--- Inventario actual ---")
    for prod in inventario:
        subtotal = prod["stock"] * prod["precio"]
        print(f"[{prod['referencia']}] {prod['nombre']}: {prod['stock']} uds x {prod['precio']:.2f} € = {subtotal:.2f} €")

    resumen = generar_resumen_inventario(inventario)

    print("\n--- Resumen del inventario ---")
    print(f"Número de referencias : {resumen['numero_referencias']}")
    print(f"Unidades totales       : {resumen['unidades_totales']}")
    print(f"Valor total            : {resumen['valor_total']:.2f} €")


if __name__ == "__main__":
    main()
