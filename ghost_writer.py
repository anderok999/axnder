from PIL import Image, ImageDraw, ImageFont
import os

def create_terminal_message(text):
    # Resolución 720p para máxima compatibilidad
    width, height = 1280, 720 
    image = Image.new('RGB', (width, height), color='black')
    draw = ImageDraw.Draw(image)
    
    # Nombre exacto del archivo que subiste
    font_filename = "Courier New.ttf"
    
    # Buscamos la fuente en la carpeta actual del script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    font_path = os.path.join(current_dir, font_filename)
    
    # Tamaño masivo: al ser una fuente real (.ttf), ahora sí obedecerá el tamaño
    # Si el texto es corto, usamos 150, si es largo bajamos a 80
    font_size = 150 if len(text) < 12 else 85

    try:
        if os.path.exists(font_path):
            font = ImageFont.truetype(font_path, font_size)
        else:
            # Si por alguna razón no está el archivo, intentamos rutas de sistema
            print(f"[!] Advertencia: {font_filename} no encontrado en carpeta local.")
            fallback_path = "/system/fonts/Roboto-Bold.ttf"
            if os.path.exists(fallback_path):
                font = ImageFont.truetype(fallback_path, font_size)
            else:
                font = ImageFont.load_default()
    except Exception as e:
        print(f"[-] Error cargando fuente: {e}")
        font = ImageFont.load_default()

    # Cálculo de centrado
    bbox = draw.textbbox((0, 0), text, font=font)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    
    # Dibujamos en verde neón centrado
    draw.text(((width - tw) // 2, (height - th) // 2), text, fill=(0, 255, 0), font=font)
    
    path = os.path.abspath("ghost_msg.png")
    image.save(path, "PNG")
    return path