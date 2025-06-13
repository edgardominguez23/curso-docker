# 🚀 Go Web App

Aplicación web mínima escrita en Go. 

---

## 📦 Requisitos

- Go 1.22+
- Docker (opcional)
- `make` (opcional)

---

## 🛠️ Instalación y ejecución local

```bash
# Clona el repositorio
git clone https://github.com/edgardominguez23/curso-docker.git
cd best_practices

# Inicializa y descarga dependencias
go mod tidy

# Compila el binario
go build -o main

# Ejecuta la aplicación
./main
```

## 🛠️ Instalación y ejecución local
```bash
# Construye la imagen (usa etiqueta versionada, no 'latest')
docker build -t go-web-app:1.0.0 .

# Ejecuta el contenedor
docker run -d -p 8080:8080 --name goapp go-web-app:1.0.0
```

## 🧪 Rutas disponibles

| Método | Ruta      | Descripción                       |
| ------ | --------- | --------------------------------- |
| GET    | `/`       | Página HTML de bienvenida         |
| GET    | `/health` | JSON con estado de salud |


