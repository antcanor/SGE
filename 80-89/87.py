"""Crea una función que reciba datos de producto y devuelva solo los campos permitidos: nombre, precio y activo."""

def preparar_datos_producto(datos):
    campos_permitidos = ["nombre", "precio", "activo"]
    return {campo: datos[campo] for campo in campos_permitidos}


def main():
    datos_completos = {
        "id": 105,
        "nombre": "Teclado",
        "precio": 79.99,
        "activo": True,
        "coste_fabricacion": 35.00,
        "proveedor": "LogiTech",
        "stock": 42
    }

    print("Datos originales recibidos:")
    print(datos_completos)

    datos_preparados = preparar_datos_producto(datos_completos)
    print("\nSolo campos permitidos):")
    print(datos_preparados)


if __name__ == "__main__":
    main()
