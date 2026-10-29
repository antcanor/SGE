"""Divide una lista en páginas de tamaño 3 y muestra cada página."""

def dividir_en_paginas(lista, tamano_pagina=3):
    paginas = []
    for i in range(0, len(lista), tamano_pagina):
        pedazo = lista[i: i + tamano_pagina]
        paginas.append(pedazo)
    return paginas


def main():
    elementos = [
        "Producto 1",
        "Producto 2",
        "Producto 3",
        "Producto 4",
        "Producto 5",
        "Producto 6",
        "Producto 7",
        "Producto 8",
    ]

    tamano = 3
    paginas = dividir_en_paginas(elementos, tamano_pagina=tamano)

    print(f"Total de elementos: {len(elementos)} (tamaño de página: {tamano})\n")
    for numero_pagina, pagina in enumerate(paginas, start=1):
        print(f"Página {numero_pagina}: {pagina}")


if __name__ == "__main__":
    main()
