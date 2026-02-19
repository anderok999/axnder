import os
import random
import ghost_writer
import voice_engine

def obtener_puerto_libre():
    """Genera un puerto aleatorio para evitar colisiones en Android/Termux."""
    return random.randint(9000, 9800)

def run_payload(ip, file_path, sistema):
    puerto = obtener_puerto_libre()
    print(f"[*] Usando puerto dinámico: {puerto}")
    os.system(f"nanodlna play --device {ip} {file_path} --port {puerto}")

def run_ghost_write(ip, text, sistema):
    puerto = obtener_puerto_libre()
    img_path = ghost_writer.create_terminal_message(text)
    print(f"[*] Usando puerto dinámico: {puerto}")
    print(f"[*] Enviando interfaz visual a {ip}...")
    os.system(f"nanodlna play --device {ip} {img_path} --port {puerto}")

def run_ghost_voice(ip, text, sistema):
    puerto = obtener_puerto_libre()
    img_path = ghost_writer.create_terminal_message(text)
    audio_path = voice_engine.generate_voice(text)
    print(f"[*] Usando puerto dinámico: {puerto}")
    print(f"[*] Ejecutando Ghost Voice en {ip}...")
    # Enviamos imagen y luego audio
    os.system(f"nanodlna play --device {ip} {img_path} --port {puerto}")
    # Usamos un puerto distinto para el audio para evitar solapamiento
    os.system(f"nanodlna play --device {ip} {audio_path} --port {puerto + 1}")