import os
import platform
import sys
import subprocess
import re
from branding import show_banner
import injector

def limpiar_pantalla(sistema):
    if sistema == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def buscar_tv_automatica(sistema):
    """Escanea la red local buscando dispositivos activos."""
    print(f"[*] Iniciando escaneo de red en modo {sistema}...")
    dispositivos = []
    
    try:
        # Comando según el sistema operativo
        # Windows usa 'arp -a', Termux/Linux prefiere 'ip neighbor'
        cmd = "arp -a" if sistema == "Windows" else "ip neighbor show"
        scan = subprocess.check_output(cmd, shell=True, stderr=subprocess.DEVNULL).decode("utf-8")
        
        # Filtro Regex para extraer direcciones IPv4
        ips_encontradas = re.findall(r'[0-9]+(?:\.[0-9]+){3}', scan)
        
        # Eliminamos duplicados y filtramos la IP del router (comúnmente .1 o .254)
        dispositivos = sorted(list(set([ip for ip in ips_encontradas if not ip.endswith((".1", ".254"))])))
        
    except Exception as e:
        print(f"[!] Error durante el escaneo: {e}")

    if dispositivos:
        print(f"\n[+] Dispositivos detectados en tu red:")
        for i, ip in enumerate(dispositivos):
            print(f"  [{i}] Target IP: {ip}")
        
        print(f"  [{len(dispositivos)}] Introducir IP manualmente")
        
        sel = input("\n[AXNDER] Selecciona un índice: ")
        
        if sel.isdigit():
            idx = int(sel)
            if idx < len(dispositivos):
                return dispositivos[idx]
        
        # Si elige el último índice o pone algo no válido, pide manual
        return input("[+] Introduce la IP manualmente: ")
    else:
        print("[!] No se detectaron dispositivos automáticamente.")
        return input("[+] Introduce la IP de la TV manualmente: ")

def main():
    # 1. Identificación de Entorno
    sistema_actual = platform.system()
    limpiar_pantalla(sistema_actual)
    
    # 2. Branding AXNDER
    show_banner()
    print(f"--- [MODO: {sistema_actual.upper()}] ---")
    print("Estableciendo protocolos RNIBO...\n")

    # 3. Escaneo Automático de Objetivo
    target_ip = buscar_tv_automatica(sistema_actual)
    
    if not target_ip:
        print("[!] Error: No se definió un objetivo. Abortando.")
        return

    print(f"\n[*] Objetivo fijado: {target_ip}")
    print("-" * 40)

    # 4. Menú de Operaciones
    print("[1] Inyección RNIBO (Video Intro + Payload)")
    print("[2] Ghost Write (Texto Gigante en Pantalla)")
    print("[3] Ghost Voice (Texto + Voz TTS)")
    print("[4] Cambiar Objetivo (Rescanear)")
    print("[5] Salir")
    
    opcion = input("\n[AXNDER-MINERANDER]>> ")

    if opcion == "5":
        print("Cerrando sesión del sistema...")
        sys.exit()
    elif opcion == "4":
        return main() # Reinicia para volver a escanear

    # 5. Ejecución de Módulos vía Injector
    if opcion == "1":
        injector.run_payload(target_ip, "intro_axnder.mp4", sistema_actual)
    elif opcion == "2":
        msg = input("[?] MENSAJE VISUAL: ")
        injector.run_ghost_write(target_ip, msg, sistema_actual)
    elif opcion == "3":
        msg = input("[?] MENSAJE PARA VOZ: ")
        injector.run_ghost_voice(target_ip, msg, sistema_actual)
    else:
        print("[!] Opción inválida.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n[!] Operación cancelada por el usuario.")
        sys.exit()