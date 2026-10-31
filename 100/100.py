"""Crea una función que genere referencias del tipo PROD-0001 a partir de un número entero."""

def generar_referencia(numero):
    return f"PROD-{numero:04d}"


def main():
    numeros_prueba = [1, 25, 342, 999, 1000]

    print("Generación de referencias automáticas:")
    for num in numeros_prueba:
        referencia = generar_referencia(num)
        print(f"Número: {num} -> Referencia: {referencia}")


if __name__ == "__main__":
    main()
