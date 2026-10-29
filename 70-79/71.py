"""Convierte un diccionario de cliente a JSON y vuelve a convertirlo a diccionario."""

import json

def main():
    cliente = {
        "id": 1045,
        "nombre": "Antonio",
        "email": "antonio@prueba.com",
        "activo": True,
        "saldo": 150.75
    }

    cliente_json = json.dumps(cliente, indent=4, ensure_ascii=False)

    print("--- Cadena JSON Resultante ---")
    print(cliente_json)

    cliente_diccionario = json.loads(cliente_json)

    print("--- Diccionario ---")
    print(cliente_diccionario)


if __name__ == "__main__":
    main()
