"""Calcula el stock disponible como stock físico menos unidades reservadas; no permitas resultados negativos."""

def calcular_disponibilidad(stock_fisico, unidades_reservadas):
    disponible = stock_fisico - unidades_reservadas
    return max(0, disponible)


def main():
    casos_prueba = [
        {"fisico": 50, "reservadas": 20},
        {"fisico": 15, "reservadas": 15},
        {"fisico": 5, "reservadas": 12},
        {"fisico": 0, "reservadas": 5}
    ]

    print("Cálculo de disponibilidad de stock:")
    for caso in casos_prueba:
        fisico = caso["fisico"]
        reservadas = caso["reservadas"]
        disponible = calcular_disponibilidad(fisico, reservadas)
        print(f"Físico: {fisico:2d} | Reservadas: {reservadas:2d} -> Disponible: {disponible:2d}")


if __name__ == "__main__":
    main()
