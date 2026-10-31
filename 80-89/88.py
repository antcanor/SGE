"""Define transiciones permitidas: borrador→confirmado, confirmado→enviado y enviado→entregado. Valida una transición."""

TRANSICIONES_PERMITIDAS = {
    "borrador": ["confirmado"],
    "confirmado": ["enviado"],
    "enviado": ["entregado"]
}

def validar_transicion(estado_actual, nuevo_estado):
    estados_posibles = TRANSICIONES_PERMITIDAS.get(estado_actual, [])
    return nuevo_estado in estados_posibles


def main():
    pruebas = [
        ("borrador", "confirmado"),
        ("confirmado", "enviado"),
        ("enviado", "entregado"),
        ("borrador", "enviado"),
        ("confirmado", "borrador"),
        ("entregado", "enviado"),
        ("cancelado", "confirmado")
    ]

    print("Comprobación de transiciones de estado:")
    for actual, nuevo in pruebas:
        valida = validar_transicion(actual, nuevo)
        estado = "VÁLIDA" if valida else "NO PERMITIDA"
        print(f"Transición '{actual}' -> '{nuevo}': {estado}")


if __name__ == "__main__":
    main()
