#!/bin/bash

# Nombre de la imagen de Docker
IMAGE_NAME="ayf:python3.12"

# Construye la imagen de Docker
echo "Construyendo la imagen Docker..."
docker build -t $IMAGE_NAME .

# Verifica si la construcción fue exitosa
if [ $? -eq 0 ]; then
    echo "Imagen construida correctamente."
else
    echo "Error en la construcción de la imagen."
    exit 1
fi

# Ejecuta el contenedor Docker
echo "Ejecutando el contenedor Docker..."
docker run -d -p 3000:3000 $IMAGE_NAME