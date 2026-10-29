"""Guarda una lista de productos en un archivo CSV con cabeceras"""
import csv

def main():
    productos = [
        {"ID": 1, "Nombre": "Portatil", "Precio": 850.00, "Stock": 15},
        {"ID": 2, "Nombre": "Ratón Óptico", "Precio": 22.50, "Stock": 50},
        {"ID": 3, "Nombre": "Teclado Mecánico", "Precio": 75.00, "Stock": 30},
        {"ID": 4, "Nombre": "Monitor 24''", "Precio": 145.99, "Stock": 12}
    ]

    archivo_csv = "productos.csv"
    cabeceras = ["ID", "Nombre", "Precio", "Stock"]

    try:
        with open(archivo_csv, mode="w", newline="", encoding="utf-8") as archivo:
            # Se crea el objeto escritor especificando las cabeceras
            escritor = csv.DictWriter(archivo, fieldnames=cabeceras)

            # Escribe la línea de cabeceras
            escritor.writeheader()

            # Escribe todas las filas de productos
            escritor.writerows(productos)

        print(f"Archivo '{archivo_csv}' guardado con éxito.")

    except IOError:
        print("Ocurrió un error al intentar escribir el archivo.")



if __name__ == "__main__":
    main()
