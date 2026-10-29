"""Con una lista de diccionarios, crea una función buscar que acepte un criterio de campo y valor."""

def buscar_por_campo_valor(lista, campo, valor):
    return [linea for linea in lista if linea.get(campo) == valor]

def main():
    lista = [
        {"id": 1, "nombre": "Teclado Mecánico", "categoría": "Periféricos", "precio": 75.00},
        {"id": 2, "nombre": "Ratón Óptico", "categoría": "Periféricos", "precio": 22.50},
        {"id": 3, "nombre": "Monitor 24''", "categoría": "Pantallas", "precio": 145.99},
        {"id": 4, "nombre": "Auriculares", "categoría": "Audio", "precio": 45.00},
        {"id": 5, "nombre": "Altavoces", "categoría": "Audio", "precio": 75.00}
    ]

    productos_audio = buscar_por_campo_valor(lista, campo="categoría", valor="Audio")
    print("--- Productos de Audio ---")
    print(productos_audio)

    productos_75 = buscar_por_campo_valor(lista, campo="precio", valor=75.00)
    print("\n--- Productos de 75 € ---")
    print(productos_75)

if __name__ == "__main__":
    main()
