"""Calcula el total de varias líneas de pedido, aplicando a cada línea su tipo de IVA."""

def main():
    lineas_pedido = [
        {"producto": "Libro educativo", "cantidad": 2, "precio_unitario": 15.00, "iva": 0.04},
        {"producto": "Paquete de café", "cantidad": 3, "precio_unitario": 4.50, "iva": 0.10},
        {"producto": "Auriculares Bluetooth", "cantidad": 1, "precio_unitario": 59.90, "iva": 0.21},
        {"producto": "Suscripción Digital", "cantidad": 1, "precio_unitario": 9.99, "iva": 0.21}
    ]

    total_base_imponible = 0.0
    total_iva = 0.0

    for linea in lineas_pedido:
        base_linea = linea["cantidad"] * linea["precio_unitario"]
        iva_linea = base_linea * linea["iva"]
        total_linea = base_linea + iva_linea

        total_base_imponible += base_linea
        total_iva += iva_linea


    total_pedido = total_base_imponible + total_iva

    print("\n--- TOTAL ---")
    print(f"Total Base Imponible: {total_base_imponible:,.2f}€")
    print(f"Total IVA acumulado:  {total_iva:,.2f}€")
    print(f"TOTAL A PAGAR:        {total_pedido:,.2f}€")

if __name__ == "__main__":
    main()
