import subprocess
import sys
import os

def install_dependencies():
    print("\033[96m[*] INICIANDO INSTALADOR AXNDER-MINERANDER...\033[0m")
    try:
        # Instala las librerías desde el archivo requirements.txt
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("\033[92m[+] TODAS LAS DEPENDENCIAS SE INSTALARON CORRECTAMENTE.\033[0m")
    except Exception as e:
        print(f"\033[91m[-] ERROR DURANTE LA INSTALACIÓN: {e}\033[0m")
        sys.exit(1)

def check_files():
    # Verifica que los archivos críticos existan
    files = ["main.py", "injector.py", "branding.py", "ghost_writer.py", "voice_engine.py", "intro_axnder.mp4"]
    for f in files:
        if os.path.exists(f):
            print(f"\033[92m[OK]\033[0m {f} detectado.")
        else:
            print(f"\033[93m[WARN]\033[0m {f} no se encuentra en la carpeta.")

if __name__ == "__main__":
    install_dependencies()
    check_files()
    print("\n\033[96m[*] SISTEMA LISTO. EJECUTANDO MAIN...\033[0m\n")
    time_sleep = 2
    # Lanza automáticamente el programa principal después de instalar
    subprocess.run([sys.executable, "main.py"])