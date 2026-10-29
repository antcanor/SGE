"""Detecta códigos de producto duplicados en una lista."""

def detectar_codigos_duplicados(productos):
    vistos = []
    duplicados = []
    for producto in productos:
        if producto in vistos:
            duplicados.append(producto)
        elif producto in duplicados:
            pass
        else:
            vistos.append(producto)
    return duplicados

def main():
    productos = ["PROD-101", "PROD-202", "PROD-101", "PROD-303", "PROD-202", "PROD-404"]

    codigos_repetidos = detectar_codigos_duplicados(productos)

    print(f"Códigos duplicados encontrados: {codigos_repetidos}")

if __name__ == "__main__":
    main()
