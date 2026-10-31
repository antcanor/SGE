"""Implementa funciones para añadir productos, buscar por código y listar productos activos. Controla códigos duplicados."""

def buscar_por_codigo(catalogo, codigo):
    for producto in catalogo:
        if producto.get("codigo") == codigo:
            return producto
    return None


def anadir_producto(catalogo, producto):
    codigo = producto.get("codigo")
    if buscar_por_codigo(catalogo, codigo) is not None:
        return False
    catalogo.append(producto)
    return True


def listar_productos_activos(catalogo):
    return [p for p in catalogo if p.get("activo") is True]


def main():
    catalogo = []

    # 1. Añadir productos iniciales
    productos_a_insertar = [
        {"codigo": "ART-01", "nombre": "Teclado USB", "precio": 19.99, "activo": True},
        {"codigo": "ART-02", "nombre": "Ratón Óptico", "precio": 12.50, "activo": True},
        {"codigo": "ART-03", "nombre": "Cable HDMI 2m", "precio": 6.00, "activo": False},
        {"codigo": "ART-04", "nombre": "Hub USB-C", "precio": 24.90, "activo": True},
    ]

    print("--- Añadiendo productos al catálogo ---")
    for prod in productos_a_insertar:
        if anadir_producto(catalogo, prod):
            print(f"Producto '{prod['codigo']}' ({prod['nombre']}) añadido correctamente.")
        else:
            print(f"Error: No se pudo añadir el producto con código '{prod['codigo']}'.")

    # 2. Controlar código duplicado
    producto_duplicado = {"codigo": "ART-02", "nombre": "Ratón Gaming Láser", "precio": 35.00, "activo": True}
    print("\n--- Intentando añadir producto con código duplicado ('ART-02') ---")
    if anadir_producto(catalogo, producto_duplicado):
        print("Producto añadido con éxito.")
    else:
        print(f"Operación rechazada: Ya existe un producto con el código '{producto_duplicado['codigo']}'.")

    # 3. Buscar por código
    print("\n--- Búsqueda por código ---")
    busqueda_1 = buscar_por_codigo(catalogo, "ART-01")
    print(f"Buscar 'ART-01': {busqueda_1}")

    busqueda_2 = buscar_por_codigo(catalogo, "ART-99")
    print(f"Buscar 'ART-99' (inexistente): {busqueda_2}")

    # 4. Listar productos activos
    print("\n--- Listado de productos activos ---")
    activos = listar_productos_activos(catalogo)
    for p in activos:
        print(f"- [{p['codigo']}] {p['nombre']}: {p['precio']:.2f} €")


if __name__ == "__main__":
    main()
