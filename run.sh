#!/bin/bash

# Nombre de la imagen
IMAGE_NAME="aguas-news"

# Función para construir la imagen
build_image() {
    echo "Construyendo la imagen Docker..."
    docker build -t $IMAGE_NAME .
}

# Comprobar si el primer argumento es "build"
if [ "$1" == "build" ]; then
    build_image
else
    # Comprobar si la imagen existe
    if ! docker image inspect $IMAGE_NAME > /dev/null 2>&1; then
        echo "La imagen '$IMAGE_NAME' no existe. Iniciando construcción..."
        build_image
    fi
fi

# Ejecutar el contenedor con el volumen montado
echo "Obteniendo noticias......"
docker run --rm --env-file .env -v "$(pwd)/output":/usr/src/app/output $IMAGE_NAME
