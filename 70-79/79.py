"""Refactoriza un cálculo de total para que la función reciba datos
y devuelva un resultado, sin usar input ni print dentro."""

def calcular_total_pedido(lineas_pedido) :

    return sum(linea["cantidad"] * linea["precio_unitario"] for linea in lineas_pedido)

def main():
    datos_pedido = [
        {"producto": "Teclado", "cantidad": 2, "precio_unitario": 75.00},
        {"producto": "Ratón", "cantidad": 1, "precio_unitario": 22.50},
        {"producto": "Alfombrilla", "cantidad": 3, "precio_unitario": 15.00}
    ]
    resultado_total = calcular_total_pedido(datos_pedido)
    print(f"El total calculado es: {resultado_total:,.2f}€")

if __name__ == "__main__":
    main()
