# Cambia el directorio actual a la carpeta llamada "ejercicio5".
cd ../ejercicio5

# Construye una imagen Docker a partir del Dockerfile que está en el directorio actual.
docker build -t ml-api .

# Lanza un contenedor a partir de la imagen "ml-api".
docker run -p 5000:5000 ml-api

# Lanza peticiones HTTP desde la terminal.
curl -X POST -H "Content-Type: application/json" \
    -d '{"data":[1,2,3,4]}' http://localhost:5000/predict
