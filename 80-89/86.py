"""Crea una función que permita borrar un registro solo si el usuario tiene rol 'administrador'."""

def borrar_registro(usuario, registro, lista_registros):
    if usuario.get("rol") != "administrador":
        return False

    if registro in lista_registros:
        lista_registros.remove(registro)
        return True

    return False


def main():
    registros = [
        {"id": 1, "nombre": "Producto A"},
        {"id": 2, "nombre": "Producto B"},
        {"id": 3, "nombre": "Producto C"}
    ]

    usuario_empleado = {"nombre": "Carlos", "rol": "empleado"}
    usuario_admin = {"nombre": "Ana", "rol": "administrador"}

    registro_a_borrar = registros[1]

    print("--- Borrar con usuario empleado ---")
    exito = borrar_registro(usuario_empleado, registro_a_borrar, registros)
    print(f"¿Borrado con éxito?: {exito}")
    print(f"Registros actuales: {registros}")

    print("\n--- Borrar con usuario administrador ---")
    exito = borrar_registro(usuario_admin, registro_a_borrar, registros)
    print(f"¿Borrado con éxito?: {exito}")
    print(f"Registros actuales: {registros}")


if __name__ == "__main__":
    main()
