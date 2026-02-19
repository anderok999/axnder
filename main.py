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
    sistema_actual = platform.system()
    limpiar_pantalla(sistema_actual)
    
    show_banner()
    print(f"--- [MODO: {sistema_actual.upper()}] ---")
    print("Iniciando suite AXNDER-MINERANDER v3.1...\n")

    print("[1] Inyección RNIBO (Video Intro + Payload)")
    print("[2] Ghost Write (Texto Gigante en Pantalla)")
    print("[3] Ghost Voice (Texto + Voz TTS)")
    print("[4] Salir")
    
    opcion = input("\n[AXNDER-MINERANDER]>> ")

    if opcion == "4":
        print("Cerrando sesión...")
        sys.exit()

    target_ip = input("[+] Introduce la IP de la TV: ")

    if opcion == "1":
        injector.run_payload(target_ip, "intro_axnder.mp4", sistema_actual)
    elif opcion == "2":
        msg = input("[?] MENSAJE VISUAL: ")
        injector.run_ghost_write(target_ip, msg, sistema_actual)
    elif opcion == "3":
        msg = input("[?] MENSAJE PARA VOZ: ")
        injector.run_ghost_voice(target_ip, msg, sistema_actual)
    else:
        print("Opción no válida.")

if __name__ == "__main__":
    main()