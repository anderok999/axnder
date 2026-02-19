import os
import ghost_writer
import voice_engine

def limpiar_puerto(sistema):
    """Intenta liberar el puerto 9000 según el sistema."""
    try:
        if sistema == "Windows":
            os.system("for /f \"tokens=5\" %a in ('netstat -aon ^| findstr :9000') do taskkill /f /pid %a >nul 2>&1")
            return "9000"
        else:
            # En Android/Termux, si fuser falla, devolvemos un puerto alternativo
            resultado = os.system("fuser -k 9000/tcp > /dev/null 2>&1")
            if resultado != 0:
                # Si no hay permisos para matar procesos, usamos el 9500
                return "9500"
            return "9000"
    except:
        return "9500"

def run_payload(ip, file_path, sistema):
    puerto = limpiar_puerto(sistema)
    print(f"[*] Inyectando payload en puerto {puerto}...")
    os.system(f"nanodlna play --device {ip} {file_path} --port {puerto}")

def run_ghost_write(ip, text, sistema):
    puerto = limpiar_puerto(sistema)
    img_path = ghost_writer.create_terminal_message(text)
    print(f"[*] Enviando mensaje visual a {ip}...")
    os.system(f"nanodlna play --device {ip} {img_path} --port {puerto}")

def run_ghost_voice(ip, text, sistema):
    puerto = limpiar_puerto(sistema)
    # Genera imagen y audio
    img_path = ghost_writer.create_terminal_message(text)
    audio_path = voice_engine.generate_voice(text)
    
    print(f"[*] Ejecutando Ghost Voice en {ip}...")
    # Primero enviamos la imagen y luego el audio (o viceversa según prefieras)
    os.system(f"nanodlna play --device {ip} {img_path} --port {puerto}")
    os.system(f"nanodlna play --device {ip} {audio_path} --port {puerto}")