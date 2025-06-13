# Cambia el directorio actual a la carpeta llamada "ejercicio6".
cd ../ejercicio6

# Construcción de imagen y contenedor
docker-compose up --build

# Creamos la tabla users en la tabla de mysql
docker exec -i $(docker ps -qf "name=ejercicio6-db-1") \
  mysql -uuser -ppassword testdb -e "CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100));"

# Agregamos el usuario Ana
curl -X POST -H "Content-Type: application/json" \
  -d '{"name":"Ana"}' http://localhost:5000/users

# Agregamos el usuario Luis
curl -X POST -H "Content-Type: application/json" \
  -d '{"name":"Luis"}' http://localhost:5000/users

# Solicitamos el listado de usuarios almacenados en mysql
curl http://localhost:5000/users
