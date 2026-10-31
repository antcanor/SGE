"""Simula un dominio sencillo como lista de condiciones (campo, operador, valor) y filtra productos."""

def evaluar_condicion(producto, campo, operador, valor):
    if campo not in producto:
        return False

    valor_producto = producto[campo]

    if operador in ("=", "=="):
        return valor_producto == valor
    elif operador == "!=":
        return valor_producto != valor
    elif operador == ">":
        return valor_producto > valor
    elif operador == ">=":
        return valor_producto >= valor
    elif operador == "<":
        return valor_producto < valor
    elif operador == "<=":
        return valor_producto <= valor
    elif operador == "in":
        return valor_producto in valor
    else:
        raise ValueError(f"Operador '{operador}' no soportado.")


def buscar_con_dominio(productos, dominio):
    resultados = []
    for producto in productos:
        cumple_todas = True
        for campo, operador, valor in dominio:
            if not evaluar_condicion(producto, campo, operador, valor):
                cumple_todas = False
                break
        if cumple_todas:
            resultados.append(producto)
    return resultados


def main():
    catalogo = [
        {"codigo": "P01", "nombre": "Teclado Mecánico", "categoria": "Periféricos", "precio": 45.0, "stock": 15, "activo": True},
        {"codigo": "P02", "nombre": "Ratón Gaming", "categoria": "Periféricos", "precio": 55.0, "stock": 8, "activo": True},
        {"codigo": "P03", "nombre": "Monitor 27\"", "categoria": "Pantallas", "precio": 199.99, "stock": 5, "activo": True},
        {"codigo": "P04", "nombre": "Auriculares USB", "categoria": "Audio", "precio": 29.99, "stock": 20, "activo": True},
        {"codigo": "P05", "nombre": "Alfombrilla", "categoria": "Periféricos", "precio": 12.50, "stock": 0, "activo": False},
        {"codigo": "P06", "nombre": "Altavoces Bluetooth", "categoria": "Audio", "precio": 49.0, "stock": 12, "activo": True},
    ]

    # Dominio 1: Periféricos activos con precio menor a 50 €
    dominio_1 = [
        ("categoria", "=", "Periféricos"),
        ("activo", "=", True),
        ("precio", "<", 50.0)
    ]
    print("--- Dominio 1: Periféricos activos con precio < 50 € ---")
    for prod in buscar_con_dominio(catalogo, dominio_1):
        print(f"- {prod['nombre']} ({prod['precio']:.2f} €)")

    # Dominio 2: Stock mayor o igual a 10 y categoría en ['Audio', 'Periféricos']
    dominio_2 = [
        ("stock", ">=", 10),
        ("categoria", "in", ["Audio", "Periféricos"])
    ]
    print("\n--- Dominio 2: Stock >= 10 en Audio o Periféricos ---")
    for prod in buscar_con_dominio(catalogo, dominio_2):
        print(f"- {prod['nombre']} | Categ: {prod['categoria']} | Stock: {prod['stock']}")


if __name__ == "__main__":
    main()
