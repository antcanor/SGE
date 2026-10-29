"""Crea funciones para normalizar un nombre (quitar espacios y convertir a título) y para validar que no quede vacío."""

def procesar_y_validar_nombre(nombre) :
    nombre_limpio = " ".join(nombre.split()).title()
    return nombre_limpio


def main():
    casos_prueba = [
        "   ana   maría  ",
        "lucas pérez",
    ]
    for caso in casos_prueba:

        resultado = procesar_y_validar_nombre(caso)
        print(f"Antiguo nombre: {caso}.-> Nuevo nombre: {resultado}")

if __name__ == "__main__":
    main()
