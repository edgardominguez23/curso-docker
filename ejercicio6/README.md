docker-compose up --build

docker exec -i $(docker ps -qf "name=ejercicio6-db-1") \
  mysql -uuser -ppassword testdb -e "CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100));"


curl -X POST -H "Content-Type: application/json" \
  -d '{"name":"Ana"}' http://localhost:5000/users

curl -X POST -H "Content-Type: application/json" \
  -d '{"name":"Luis"}' http://localhost:5000/users


curl http://localhost:5000/users
