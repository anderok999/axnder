from gtts import gTTS
import os

def generate_voice_msg(text, filename="voice_payload.mp3"):
    print(f"[*] Sintetizando voz: '{text}'...")
    # Creamos el audio en español
    tts = gTTS(text=text, lang='es')
    tts.save(filename)
    return filename