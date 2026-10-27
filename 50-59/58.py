"""Crea una función que aplique un 5 % de descuento desde 100 euros y un 10 % desde 250 euros."""

def aplicar_descuento(importe):
    if importe >= 250:
        descuento = 0.10
    elif importe >= 100:
        descuento = 0.05
    else:
        descuento = 0.0

    return importe * (1 - descuento)


def main():
    importes_prueba = [50.0, 100.0, 180.0, 250.0, 320.0]

    for importe in importes_prueba:
        total_con_descuento = aplicar_descuento(importe)
        ahorro = importe - total_con_descuento
        porcentaje = (ahorro / importe) * 100 if importe > 0 else 0
        print(
            f"Importe: {importe:6.2f} € | "
            f"Descuento: {porcentaje:2.0f}% ({ahorro:5.2f} €) | "
            f"Total a pagar: {total_con_descuento:6.2f} €"
        )


if __name__ == "__main__":
    main()
