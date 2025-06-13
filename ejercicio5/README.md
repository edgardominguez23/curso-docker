cd ../ejercicio5

docker build -t ml-api .

docker run -p 5000:5000 ml-api

curl -X POST -H "Content-Type: application/json" \
    -d '{"data":[1,2,3,4]}' http://localhost:5000/predict
