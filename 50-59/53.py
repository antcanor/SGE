"""Comprueba de forma básica que una cadena contiene '@' y un punto después de ella."""

def ejercicio(correo):
    resultado = False
    punto = correo.find("@")
    if correo[punto+1]==".":
        resultado = True
    return resultado
def main():
    print(ejercicio("antonio@.com"))

if __name__ == "__main__":
    main()
