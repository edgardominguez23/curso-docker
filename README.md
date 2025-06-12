# 🐳 Manual de Instalación de Docker en Windows 10 y 11

Este documento detalla el proceso de instalación de Docker Desktop en sistemas operativos Windows 10 y 11.

---

## ✅ Requisitos del sistema

### Para Windows 10
- Edición: **Windows 10 Pro, Enterprise o Education** (Build 15063 o superior)
- **WSL 2 habilitado** (Subsistema de Windows para Linux)
- Virtualización habilitada en BIOS

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
## 🛠 Paso 3: Instalar WSL 2 manualmente

Si no se instaló automáticamente, puedes instalar WSL 2 manualmente (la distribución de Linux instalada será Ubuntu):

   ```bash
   wsl --install
   ```

Para instalar otra distribución de Linux en WSL (Windows Subsystem for Linux), ver las que están disponibles, y cambiar entre ellas, sigue estos pasos:
Abre PowerShell o el Símbolo del sistema (CMD) como administrador y ejecuta:

Con el siguiente comando listara las distibuciones disponibles para su instalación.
   ```bash
   wsl --list --online
   ```
Para la instalación de alguna distibucion listada:
   ```bash
   wsl --update
   wsl --install -d Debian
   ```
---

## 🧪 Paso 4: Verificar instalación
## 🔧 Paso 4.1: Configurar integración con WSL

### ⚙️ Configurar WSL Integration

1. Abre Docker Desktop.
2. Ve a `Settings` → `Resources` → `WSL Integration`.
3. Marca las distribuciones de WSL en las que deseas usar Docker.
4. Haz clic en `Apply & Restart` si es necesario.

Esto permite que Docker funcione de manera integrada dentro de tus entornos WSL (como Ubuntu, Debian, etc.).

## Paso 4.2: Validar instalación y configuración
1. Abre Docker Desktop desde el menú de inicio.
2. Espera a que aparezca el icono de Docker en la bandeja del sistema (barra inferior derecha).
3. Abre una terminal (PowerShell o CMD) y ejecuta:

   ```bash
   docker --version
   ```


