"""Prueba una función que calcula el precio medio: debe devolver None si no recibe precios."""

def calcular_precio_medio(precios):
    if not precios:
        return None

    return sum(precios) / len(precios)

def main():
    assert calcular_precio_medio([]) is None

    assert calcular_precio_medio(None) is None

    assert calcular_precio_medio([10.0, 20.0, 30.0]) == 20.0

    assert calcular_precio_medio([45.50]) == 45.50
if __name__ == "__main__":
    main()
