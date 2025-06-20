# ---------- ETAPA 1: Compilación ----------
FROM golang:1.22-alpine AS builder

# Crear directorio de trabajo
WORKDIR /src

# Copiar archivos de dependencias primero para aprovechar el cache
COPY go.mod ./

# Descargar dependencias del proyecto
RUN go mod download

# Copiar el resto del código fuente
COPY . .

# Compilar el binario (sin dependencias C, para Linux)
RUN CGO_ENABLED=0 GOOS=linux go build -o /app/main .

# ---------- ETAPA 2: Imagen mínima para producción ----------
FROM alpine:3.20@sha256:de4fe7064d8f98419ea6b49190df1abbf43450c1702eeb864fe9ced453c1cc5f

# Crear usuario y grupo sin privilegios
RUN addgroup -S appgroup && adduser -S appuser -G appgroup

# Establecer directorio de trabajo
WORKDIR /app

# Copiar binario compilado desde la etapa anterior
COPY --from=builder /app/main .

# Asignar permisos al usuario sin privilegios
RUN chown -R appuser:appgroup /app

# Cambiar al usuario sin privilegios
USER appuser

# Exponer el puerto de la aplicación (opcional)
EXPOSE 8080

# Definir chequeo de salud para saber si el contenedor está corriendo correctamente
HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
  CMD wget --spider http://localhost:8080/health || exit 1

# Comando por defecto para iniciar la app
CMD ["./main"]
