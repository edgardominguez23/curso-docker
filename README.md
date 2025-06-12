# 🐳 Manual de Instalación de Docker en Windows 10 y 11

Este documento detalla el proceso de instalación de Docker Desktop en sistemas operativos Windows 10 y 11.

---

## ✅ Requisitos del sistema

### Para Windows 11
- Cualquier edición es compatible (Home, Pro, etc.)
- WSL 2 y plataforma de máquina virtual deben estar habilitados
- Virtualización activada en BIOS

---

## 📥 Paso 1: Descargar Docker Desktop

1. Ve al sitio oficial de Docker:  
   👉 [https://www.docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop)
2. Haz clic en el botón `Download for Windows`.

---

## 🛠 Paso 2: Instalar Docker Desktop

1. Ejecuta el instalador descargado (`Docker Desktop Installer.exe`).
2. En la ventana de instalación:
   - Asegúrate de marcar la opción **"Install required components for WSL 2"**.
   - Haz clic en `Ok` o `Siguiente` para comenzar la instalación.
3. Finaliza la instalación y **reinicia tu sistema** si se solicita.

---

## 🧪 Paso 3: Verificar instalación

1. Abre Docker Desktop desde el menú de inicio.
2. Espera a que aparezca el icono de Docker en la bandeja del sistema (barra inferior derecha).
3. Abre una terminal (PowerShell o CMD) y ejecuta:

   ```bash
   docker --version
