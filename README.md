# 🛡️ AXNDER-MINERANDER v3.0

![Python](https://img.shields.io/badge/Python-3.14-blue.svg)
![Status](https://img.shields.io/badge/Status-Stable-green.svg)
![Protocol](https://img.shields.io/badge/Protocol-RNIBO-cyan.svg)

**MINERANDER** es una potente suite de control y override para dispositivos multimedia (Smart TVs, Renderers) basada en el protocolo **RNIBO**. Permite la inyección de contenido visual, mensajes de terminal dinámicos y síntesis de voz remota mediante la red local.

---

## 🚀 Funcionalidades Elite

* **Inyección RNIBO (Opción 1):** Ejecuta una secuencia de "acceso denegado" mediante un video introductorio seguido del payload final.
* **Ghost Write (Opción 2):** Modo silencioso que genera e inyecta imágenes de texto estilo terminal en tiempo real.
* **Ghost Voice (Opción 3):** Combina la generación visual con **Text-to-Speech (TTS)** para que la TV muestre un mensaje y lo lea en voz alta simultáneamente.
* **Socket Purge System:** Motor inteligente que detecta y libera el puerto **TCP 9000** mediante `netstat` para evitar colisiones de conexión (Error 10048).

---

## 🛠️ Requisitos del Sistema

El sistema utiliza un stack modular para máxima eficiencia:
* **nanodlna**: Motor principal de comunicación UPnP/DLNA.
* **Pillow (PIL)**: Para la generación dinámica de interfaces visuales.
* **gTTS**: Motor de síntesis de voz de Google.
* **Twisted**: Backend de red para el streaming de datos.



---

## 📦 Instalación Rápida

1.  **Clonar el repositorio:**
    ```bash
    git clone [https://github.com/tu-usuario/MINERANDER.git](https://github.com/tu-usuario/MINERANDER.git)
    cd MINERANDER
    ```

2.  **Ejecutar el Setup Automatizado:**
    Hemos incluido un script que prepara todo el entorno por ti:
    ```bash
    python setup.py
    ```
    *Este comando instalará las librerías necesarias y lanzará la consola AXNDER automáticamente.*

---

## 📂 Estructura del Proyecto

* `main.py`: Interfaz de usuario y lógica de control.
* `injector.py`: El corazón del sistema; gestiona los bypass de red y sockets.
* `ghost_writer.py`: Generador de imágenes para los mensajes en pantalla.
* `voice_engine.py`: Sintetizador de audio para la TV.
* `setup.py`: Instalador de dependencias y verificador de integridad.

---
## 📱 Soporte Multiplataforma (Híbrido)

Esta versión de **MINERANDER** ha sido optimizada para funcionar sin cambios en el código tanto en entornos de escritorio como móviles:

* **💻 Windows**: Utiliza comandos nativos de limpieza de puertos (`taskkill`) y gestión de terminal.
* **📱 Android (Termux)**: Sistema inteligente de bypass de permisos. Si el puerto estándar está bloqueado, el inyector cambia automáticamente a puertos de respaldo (9500+) para evitar errores de ejecución.



---

## 🛠️ Instalación en Termux (Android)

Para llevar el poder de **MINERANDER** en tu bolsillo, sigue estos pasos en tu terminal móvil:

1.  **Actualizar entorno**:
    ```bash
    pkg update && pkg upgrade
    pkg install python git psmisc
    ```
2.  **Clonar y configurar**:
    ```bash
    git clone [https://github.com/anderok999/axnder.git](https://github.com/anderok999/axnder.git)
    cd axnder
    pip install -r requirements.txt
    ```
3.  **Ejecutar**:
    ```bash
    python main.py
    ```

## ⚠️ Nota de Seguridad
Este software ha sido desarrollado con fines de investigación en protocolos de red y automatización del hogar. El autor (**AXNDER**) no se hace responsable del uso indebido de las capacidades de inyección remota del software.

---
**Desarrollado por AXNDER | 2026**