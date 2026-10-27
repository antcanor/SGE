#!/bin/bash

# Bucle principal que avanza de 10 en 10 (50, 60, 70, 80, 90, 100)
for base in {50..100..10}
do
    # El 100 es un caso especial (solo un archivo), definimos su fin en 100
    if [ $base -eq 100 ]; then
        fin=100
        CARPETA="100"
    else
        # Calcular el límite superior del rango (ej. 59 si la base es 50)
        fin=$((base + 9))
        CARPETA="${base}-${fin}"
    fi
    
    # Crear la subcarpeta
    mkdir -p "$CARPETA"
    
    # Bucle interno para crear los archivos dentro de la carpeta
    for i in $(seq $base $fin)
    do
        ARCHIVO="$CARPETA/$i.py"
        
        # Crear el archivo con su estructura main
        cat << EOF > "$ARCHIVO"
def main():
    print("Este es el archivo número $i")

if __name__ == "__main__":
    main()
EOF
    done
done

echo "¡Completado! Se han creado las carpetas por decenas hasta el archivo 100.py."
