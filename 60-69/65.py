"""Calcula cuántos días quedan hasta una fecha de vencimiento dada como AAAA-MM-DD."""

from datetime import datetime, date

def dias_hasta_vencimiento(fecha_str):
    """
    Calcula cuántos días quedan hasta una fecha de vencimiento en formato 'AAAA-MM-DD'.
    Retorna un número positivo si la fecha es futura, 0 si es hoy, o negativo si ya venció.
    """
    fecha_vencimiento = datetime.strptime(fecha_str, "%Y-%m-%d").date()
    hoy = date.today()
    return (fecha_vencimiento - hoy).days


def main():
    fechas_prueba = [
        "2026-12-31",
        date.today().strftime("%Y-%m-%d"),
        "2025-01-01",
    ]

    print(f"Fecha actual (hoy): {date.today()}\n")

    for fecha in fechas_prueba:
        dias = dias_hasta_vencimiento(fecha)
        if dias > 0:
            print(f"Para el vencimiento '{fecha}' quedan {dias} día(s).")
        elif dias == 0:
            print(f"La fecha '{fecha}' vence hoy.")
        else:
            print(f"La fecha '{fecha}' ya venció hace {abs(dias)} día(s).")


if __name__ == "__main__":
    main()
