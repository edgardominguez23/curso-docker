# Cambia el directorio actual a la carpeta llamada "ejercicio2".
cd ../ejercicio2

# Construye una imagen de Docker a partir del Dockerfile que está en el directorio actual.
docker build -t py-pandas .

# Ejecuta un contenedor a partir de la imagen llamada "py-pandas".
docker run --rm py-pandas
