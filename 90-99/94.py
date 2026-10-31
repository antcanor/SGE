"""Normaliza una lista de clientes importados: elimina espacios en nombres y correos,
pasa el correo a minúsculas y descarta nombres vacíos."""

def normalizar_clientes(clientes):
    clientes_validos = []
    for cliente in clientes:
        nombre = cliente.get("nombre", "").strip()
        correo = cliente.get("correo", "").strip().lower()

        if not nombre:
            continue

        clientes_validos.append({
            "nombre": nombre,
            "correo": correo
        })
    return clientes_validos


def main():
    importados = [
        {"nombre": "  Ana García  ", "correo": "  ANA.GARCIA@Empresa.COM "},
        {"nombre": "Carlos López", "correo": "CARLOS@GMAIL.COM"},
        {"nombre": "   ", "correo": "vacio@example.com"},  # Nombre solo espacios
        {"nombre": "", "correo": "sin_nombre@example.com"},  # Nombre vacío
        {"nombre": " Elena Ruiz ", "correo": " Elena.Ruiz@Outlook.ES  "}
    ]

    print("--- Clientes originales importados ---")
    for c in importados:
        print(c)

    normalizados = normalizar_clientes(importados)

    print("\n--- Clientes normalizados (válidos) ---")
    for c in normalizados:
        print(f"- Nombre: '{c['nombre']}' | Correo: '{c['correo']}'")


if __name__ == "__main__":
    main()
