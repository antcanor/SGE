"""Selecciona productos activos con stock mayor que cero y precio inferior a 100 euros"""
def main():
    productos = [
        {"id": 1, "nombre": "Teclado Mecánico", "precio": 75.00, "stock": 30, "activo": True},
        {"id": 2, "nombre": "Ratón Óptico", "precio": 22.50, "stock": 0, "activo": True},  # Sin stock
        {"id": 3, "nombre": "Monitor 24''", "precio": 145.99, "stock": 12, "activo": True},  # Precio >= 100
        {"id": 4, "nombre": "Alfombrilla Gaming", "precio": 15.00, "stock": 50, "activo": False},  # Inactivo
        {"id": 5, "nombre": "Auriculares", "precio": 45.00, "stock": 8, "activo": True}
    ]

    productos_filtrados = [
        p for p in productos
        if p["activo"] and p["stock"] > 0 and p["precio"] < 100
    ]

    print("Productos seleccionados:")
    for p in productos_filtrados:
        print(f"- {p['nombre']}: {p['precio']}€ (Stock: {p['stock']})")

if __name__ == "__main__":
    main()
