"""Convierte una lista de filas (diccionarios) en un diccionario indexado por código de producto."""

def indexar_por_codigo(filas, clave="codigo"):
    """Transforma una lista de diccionarios en un diccionario indexado por el código."""
    return {fila[clave]: fila for fila in filas}


def main():
    filas = [
        {"codigo": "ART-01", "nombre": "Impresora Láser", "precio": 149.99},
        {"codigo": "ART-02", "nombre": "Tóner Negro", "precio": 35.50},
        {"codigo": "ART-03", "nombre": "Paquete Papel A4", "precio": 4.95},
    ]

    print("Lista original de filas:")
    for f in filas:
        print(f"  {f}")

    productos_indexados = indexar_por_codigo(filas)

    print("\nDiccionario indexado por código:")
    for codigo, datos in productos_indexados.items():
        print(f"  '{codigo}': {datos}")

    # Ejemplo de acceso directo O(1)
    codigo_consulta = "ART-02"
    print(f"\nConsulta directa de '{codigo_consulta}': {productos_indexados[codigo_consulta]['nombre']}")


if __name__ == "__main__":
    main()
