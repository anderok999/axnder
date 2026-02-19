from branding import show_banner, clear_screen, typewriter_effect
from injector import AxnderEngine
from ghost_writer import create_terminal_message
from voice_engine import generate_voice_msg
import time

def main():
    clear_screen()
    show_banner()
    
    engine = AxnderEngine()
    typewriter_effect("\033[96m[*] INICIANDO PROTOCOLO RNIBO (SCANN V4)...\033[0m")
    
    try:
        devs = engine.scan_network()
    except Exception as e:
        print(f"\033[91m[-] ERROR DE RED: {e}\033[0m")
        return
    
    if not devs:
        print("\033[91m[-] ERROR: NO SE ENCONTRARON OBJETIVOS.\033[0m")
        return

    # Listado de TV encontradas
    print("\n ID | OBJETIVO                   | DIRECCIÓN XML")
    print(" " + "-"*65)
    for idx, d in enumerate(devs):
        name = d.get('friendly_name', 'TV') if isinstance(d, dict) else getattr(d, 'friendly_name', 'TV')
        loc = d.get('location', 'S/N') if isinstance(d, dict) else getattr(d, 'location', 'S/N')
        print(f" {idx:<2} | {name[:25]:<26} | {loc}")
    print(" " + "-"*65)

    try:
        target_id = int(input("\n[?] SELECCIONA EL ID DEL OBJETIVO: "))
        
        while True:
            print("\n\033[96m" + "—"*35)
            print("   CENTRO DE CONTROL AXNDER")
            print("—"*35 + "\033[0m")
            print(" 1. INYECTAR ARCHIVO (INTRO + PAYLOAD)")
            print(" 2. GHOST WRITE (SOLO TEXTO)")
            print(" 3. GHOST VOICE (TEXTO + VOZ)") # <-- LA NUEVA OPCIÓN
            print(" 4. ABORTAR/STOP")
            print(" 5. SALIR")
            
            opc = input("\n[AXNDER-MINERANDER]>> ")

            if opc == "1":
                file_path = input("[?] ARCHIVO (ej: 1.jpeg): ")
                engine.inject_sequence(target_id, file_path)
            
            elif opc == "2":
                # MODO SILENCIOSO (Solo lo que escribes)
                msg = input("[?] MENSAJE VISUAL: ")
                img_path = create_terminal_message(msg)
                engine.inject_direct(target_id, img_path)
                print("\033[92m[+] INTERFAZ VISUAL ENVIADA (MUDO).\033[0m")

            elif opc == "3":
                # MODO GHOST VOICE (Texto + Audio)
                msg = input("[?] MENSAJE PARA MOSTRAR Y ESCUCHAR: ")
                print("[*] Sincronizando multimedia...")
                img_path = create_terminal_message(msg)
                audio_path = generate_voice_msg(msg)
                
                # Primero mostramos el texto
                engine.inject_direct(target_id, img_path)
                # Pausa estratégica para que de tiempo a leer antes de hablar
                time.sleep(2.5) 
                # Luego mandamos el audio
                engine.inject_direct(target_id, audio_path)
                print("\033[92m[+] ATAQUE MULTIMODAL COMPLETADO.\033[0m")

            elif opc == "4":
                engine.stop_all(target_id)
                print("\033[93m[!] Proyección detenida.\033[0m")

            elif opc == "5":
                print("Cerrando sesión de comando...")
                break
            
            else:
                print("Comando inválido.")

    except Exception as e:
        print(f"[-] ERROR: {e}")

if __name__ == "__main__":
    main()