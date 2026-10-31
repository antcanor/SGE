"""Crea una función que indique si un pedido puede autorizarse:
el cliente debe estar activo y no superar su límite de crédito."""

def puede_autorizar_pedido(cliente, importe_pedido):
    if not cliente.get("activo", False):
        return False

    limite_credito = cliente.get("limite_credito", 0.0)
    deuda_actual = cliente.get("deuda", 0.0)

    return (deuda_actual + importe_pedido) <= limite_credito


def main():
    cliente_activo_solvente = {
        "nombre": "Empresa ABC",
        "activo": True,
        "limite_credito": 1000.0,
        "deuda": 200.0
    }

    cliente_inactivo = {
        "nombre": "Comercial XYZ",
        "activo": False,
        "limite_credito": 2000.0,
        "deuda": 0.0
    }

    casos = [
        (cliente_activo_solvente, 500.0, "Pedido dentro del límite"),
        (cliente_activo_solvente, 900.0, "Pedido supera límite (200 + 900 > 1000)"),
        (cliente_inactivo, 100.0, "Cliente inactivo")
    ]

    for cliente, importe, descripcion in casos:
        autorizado = puede_autorizar_pedido(cliente, importe)
        estado = "AUTORIZADO" if autorizado else "DENEGADO"
        print(f"[{estado}] {cliente['nombre']} | Pedido: {importe:.2f} € -> {descripcion}")


if __name__ == "__main__":
    main()
