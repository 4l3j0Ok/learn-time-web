#!/bin/bash
# Script para obtener determinada imagen, convertirla a webp y guardarla en los assets.
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
ASSETS_DIR="$( cd $SCRIPT_DIR/../assets && pwd)"

echo $ASSETS_DIR

read -p "URL de la imagen: " url
read -p "Nombre de la imagen: " name
if [ -z "$name" ]; then
    name="undefined"
fi

read -p "Subcarpeta de destino: " subfolder

if [ ! "/" = "${subfolder:0:1}" ]; then
    subfolder="/$subfolder"
fi

wget $url -O $ASSETS_DIR$subfolder/$name

cwebp -q 80 $ASSETS_DIR$subfolder/$name -o $ASSETS_DIR/$subfolder/$name.webp

rm $ASSETS_DIR$subfolder/$name

echo "Imagen guardada en $ASSETS_DIR$subfolder/$name.webp"
echo "Peso de la imagen: $(du -h $ASSETS_DIR$subfolder/$name.webp | cut -f1)"
