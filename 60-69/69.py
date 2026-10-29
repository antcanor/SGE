"""Lee un archivo productos.csv con cabeceras usando el módulo csv e imprime cada fila."""

import csv
import os

def leer_productos_csv(ruta_archivo):
    """Lee un archivo CSV con cabeceras y muestra cada fila en formato diccionario."""
    with open(ruta_archivo, mode="r", encoding="utf-8") as archivo:
        lector_csv = csv.DictReader(archivo)
        for fila in lector_csv:
            print(dict(fila))


def main():
    # Resolver la ruta hacia productos.csv relativo a la ubicación de este archivo
    directorio_actual = os.path.dirname(os.path.abspath(__file__))
    ruta_csv = os.path.join(directorio_actual, "productos.csv")

    if not os.path.exists(ruta_csv):
        print(f"Error: no se encontró el archivo '{ruta_csv}'.")
        return

    print(f"Leyendo '{ruta_csv}' con cabeceras:\n")
    leer_productos_csv(ruta_csv)


if __name__ == "__main__":
    main()
