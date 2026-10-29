"""Comprueba con assert que una función de descuento devuelve los resultados esperados."""

def calcular_descuento(precio_base, porcentaje_descuento) :
    if porcentaje_descuento < 0 or porcentaje_descuento > 100:
        raise ValueError("El descuento debe estar entre 0 y 100")
    return precio_base * (1 - porcentaje_descuento / 100)

def main():
    assert calcular_descuento(100.0, 10.0) == 90.0

    assert calcular_descuento(50.0, 0.0) == 50.0

    assert calcular_descuento(25.0, 100.0) == 0.0

    assert round(calcular_descuento(19.99, 15.0), 2) == 16.99

if __name__ == "__main__":
    main()
