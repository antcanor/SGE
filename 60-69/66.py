"""Escribe una función que compruebe que nombre no está vacío y que el correo contiene '@'."""

def validar_datos_cliente(nombre, correo):
    """
    Comprueba que el nombre no esté vacío y que el correo contenga '@'.
    Retorna True si ambos datos son válidos, False en caso contrario.
    """
    if not isinstance(nombre, str) or not nombre.strip():
        return False
    if not isinstance(correo, str) or "@" not in correo:
        return False
    return True


def main():
    clientes_prueba = [
        ("Antonio Ruiz", "antonio@gmail.com"),
        ("", "antonio@gmail.com"),
        ("   ", "antonio@gmail.com"),
        ("María López", "correos-arroba.com"),
        ("Carlos Gómez", "carlos@gmail.com"),
    ]

    for nombre, correo in clientes_prueba:
        es_valido = validar_datos_cliente(nombre, correo)
        estado = "Válido" if es_valido else "Inválido"
        print(f"Nombre: '{nombre}' | Correo: '{correo}' -> {estado}")


if __name__ == "__main__":
    main()
