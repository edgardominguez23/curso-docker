# Cambia el directorio actual a la carpeta llamada "ejercicio1".
cd ejercicio1

# Construye una imagen de Docker a partir del Dockerfile que está en el directorio actual.
docker build -t py-hello .

# Ejecuta un contenedor a partir de la imagen llamada "py-hello".
docker run --rm py-hello
