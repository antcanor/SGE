#!/usr/bin/env python3
"""
Lanzador interactivo de ejercicios (50 - 100)
Permite ejecutar el 'main()' de cada ejercicio secuencialmente pulsando Enter,
saltar directamente a un ejercicio específico o salir.
"""

import ast
import os
import subprocess
import sys


def obtener_descripcion(ruta_archivo):
    """Extrae el docstring inicial del archivo si existe."""
    try:
        with open(ruta_archivo, "r", encoding="utf-8") as f:
            arbol = ast.parse(f.read())
            doc = ast.get_docstring(arbol)
            if doc:
                return doc.strip().split("\n")[0]
    except Exception:
        pass
    return "Sin descripción disponible."


def recopilar_ejercicios():
    """Localiza todos los archivos de ejercicios del 50 al 100 ordenados por número."""
    directorio_base = os.path.dirname(os.path.abspath(__file__))
    ejercicios = []

    for num in range(50, 101):
        if num == 100:
            carpeta = "100"
        else:
            base = (num // 10) * 10
            carpeta = f"{base}-{base + 9}"

        ruta_relativa = os.path.join(carpeta, f"{num}.py")
        ruta_absoluta = os.path.join(directorio_base, ruta_relativa)

        if os.path.isfile(ruta_absoluta):
            ejercicios.append({
                "numero": num,
                "archivo_rel": ruta_relativa,
                "archivo_abs": ruta_absoluta,
                "descripcion": obtener_descripcion(ruta_absoluta)
            })

    return ejercicios


def ejecutar_ejercicio(ejercicio):
    """Ejecuta un ejercicio en su directorio de trabajo correspondiente."""
    print("\n" + "=" * 65)
    print(f" EJERCICIO {ejercicio['numero']}  ({ejercicio['archivo_rel']})")
    print(f" {ejercicio['descripcion']}")
    print("=" * 65 + "\n")
    sys.stdout.flush()

    directorio_ejercicio = os.path.dirname(ejercicio["archivo_abs"])

    resultado = subprocess.run(
        [sys.executable, ejercicio["archivo_abs"]],
        cwd=directorio_ejercicio
    )

    sys.stdout.flush()
    print("\n" + "-" * 65)
    return resultado.returncode


def main():
    ejercicios = recopilar_ejercicios()
    if not ejercicios:
        print("No se encontraron archivos de ejercicios.")
        return

    indice_por_numero = {ej["numero"]: i for i, ej in enumerate(ejercicios)}

    print("=================================================================")
    print("   LANZADOR INTERACTIVO DE EJERCICIOS PYTHON (50 al 100)")
    print("=================================================================")
    print(f"Total de ejercicios encontrados: {len(ejercicios)}")
    print("Controles:")
    print("  - Pulsa [Enter] para ejecutar el siguiente ejercicio.")
    print("  - Escribe un número (ej. '75') para saltar a ese ejercicio.")
    print("  - Escribe 'q' o 'salir' para terminar.\n")

    indice_actual = 0

    while indice_actual < len(ejercicios):
        ejercicio = ejercicios[indice_actual]
        ejecutar_ejercicio(ejercicio)

        # Si es el último ejercicio
        if indice_actual == len(ejercicios) - 1:
            print("\n¡Has llegado al final de todos los ejercicios (100)!")
            break

        siguiente_ejercicio = ejercicios[indice_actual + 1]["numero"]
        prompt = f"\n[Enter: Ejercicio {siguiente_ejercicio} | Nº para saltar | 'q' para salir]: "

        try:
            opcion = input(prompt).strip().lower()
        except (KeyboardInterrupt, EOFError):
            print("\n\nSaliendo del lanzador...")
            break

        if opcion in ("q", "quit", "salir", "exit"):
            print("Lanzador finalizado.")
            break
        elif opcion.isdigit():
            num_elegido = int(opcion)
            if num_elegido in indice_por_numero:
                indice_actual = indice_por_numero[num_elegido]
                continue
            else:
                print(f"El ejercicio {num_elegido} no está disponible.")
        else:
            # Pulsar Enter o entrada vacía -> avanzar al siguiente
            indice_actual += 1


if __name__ == "__main__":
    main()
