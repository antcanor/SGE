"""Crea una función que actualice varios campos de un registro (diccionario) con otro diccionario de valores."""

def actualizar_registro(registro, nuevos_valores):
    registro.update(nuevos_valores)
    return registro


def main():
    usuario = {
        "id": 101,
        "nombre": "Carlos",
        "email": "carlos@prueba.com",
        "rol": "usuario",
        "activo": True,
    }

    campos_a_cambiar = {"email": "carlos_nuevo@nuevo.com", "rol": "administrador"}

    usuario_actualizado = actualizar_registro(usuario, campos_a_cambiar)

    print(usuario_actualizado)


if __name__ == "__main__":
    main()
