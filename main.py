import os
import platform
import sys
from branding import show_banner
import injector

def limpiar_pantalla(sistema):
    if sistema == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def main():
    # 1. Identificar el Sistema Operativo
    sistema_actual = platform.system()
    limpiar_pantalla(sistema_actual)
    
    # 2. Mostrar Banner Personalizado
    show_banner()
    print(f"--- [MODO: {sistema_actual.upper()}] ---")
    print("Iniciando suite AXNDER-MINERANDER v3.0...\n")

    # 3. Menú de Opciones
    print("[1] Inyección RNIBO (Video Intro + Payload)")
    print("[2] Ghost Write (Texto Gigante en Pantalla)")
    print("[3] Ghost Voice (Texto + Voz TTS)")
    print("[4] Escanear Red Local")
    print("[5] Salir")
    
    opcion = input("\n[AXNDER-MINERANDER]>> ")

    if opcion == "5":
        print("Cerrando sesión...")
        sys.exit()

    # IP de la TV (Aquí puedes automatizar el escaneo o pedirla)
    target_ip = input("[+] Introduce la IP de la TV: ")

    if opcion == "1":
        injector.run_payload(target_ip, "intro_axnder.mp4", sistema_actual)
    elif opcion == "2":
        msg = input("Mensaje para la TV: ")
        injector.run_ghost_write(target_ip, msg, sistema_actual)
    elif opcion == "3":
        msg = input("Mensaje para voz: ")
        injector.run_ghost_voice(target_ip, msg, sistema_actual)
    else:
        print("Opción no válida.")

if __name__ == "__main__":
    main()