#!/bin/bash
# Script para obtener determinada imagen, convertirla a webp y guardarla en los assets.
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
IMAGES_DIR="$( cd $SCRIPT_DIR/../assets/images && pwd)"

echo $IMAGES_DIR

read -p "URL de la imagen: " url
read -p "Nombre de la imagen: " name
if [ -z "$name" ]; then
    name="undefined"
fi

read -p "Subcarpeta de destino: " subfolder


if [ ! -z "$subfolder" ]; then
    if [ ! "/" = "${subfolder:0:1}" ]; then
        subfolder="/$subfolder"
    fi
fi

# si no existe la carpeta se crea
if [ ! -d "$IMAGES_DIR$subfolder" ]; then
    mkdir -p $IMAGES_DIR$subfolder
fi

wget $url -O $IMAGES_DIR$subfolder/$name

cwebp -q 80 $IMAGES_DIR$subfolder/$name -o $IMAGES_DIR/$subfolder/$name.webp

rm $IMAGES_DIR$subfolder/$name

echo "Imagen guardada en $IMAGES_DIR$subfolder/$name.webp"
echo "Peso de la imagen: $(du -h $IMAGES_DIR$subfolder/$name.webp | cut -f1)"
