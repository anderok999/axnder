import os
import sys
import time

def typewriter_effect(text, speed=0.002, color='\033[96m'):
    """Efecto de escritura cinética estilo JARVIS/FRIDAY"""
    for char in text:
        sys.stdout.write(color + char + '\033[0m')
        sys.stdout.flush()
        time.sleep(speed)
    print()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_banner():
    CYAN = '\033[96m'
    RESET = '\033[0m'
    banner = f"""
{CYAN}      ███████╗ ██╗  ██╗███╗   ██╗██████╗ ███████╗██████╗ 
      ██╔══██╗╚██╗██╔╝████╗  ██║██╔══██╗██╔════╝██╔══██╗
      ███████║ ╚███╔╝ ██╔██╗ ██║██║  ██║█████╗  ██████╔╝
      ██╔══██║ ██╔██╗ ██║╚██╗██║██║  ██║██╔══╝  ██╔══██╗
      ██║  ██║██╔╝ ██╗██║ ╚████║██████╔╝███████╗██║  ██║
      ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝{RESET}"""
    typewriter_effect(banner, 0.001)
    typewriter_effect(" > PROTOCOLO RNIBO INICIALIZADO...")
    typewriter_effect(" > SISTEMA AXNDER-MINERANDER: ONLINE")
    print(f"{CYAN}" + "—"*60 + f"{RESET}")