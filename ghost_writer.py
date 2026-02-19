from PIL import Image, ImageDraw, ImageFont
import os

def create_terminal_message(text):
    # Resolución Full HD
    width, height = 1920, 1080
    image = Image.new('RGB', (width, height), color='black')
    draw = ImageDraw.Draw(image)
    
    # Lista extendida de fuentes para Android y Windows
    font_paths = [
        "/system/fonts/Roboto-Bold.ttf",
        "/system/fonts/DroidSans-Bold.ttf",
        "C:\\Windows\\Fonts\\arialbd.ttf",
        "arial.ttf"
    ]

    font_path = None
    for path in font_paths:
        if os.path.exists(path):
            font_path = path
            break

    font_size = 200 # Tamaño masivo
    try:
        if font_path:
            font = ImageFont.truetype(font_path, font_size)
        else:
            font = ImageFont.load_default()
            print("[!] Advertencia: Usando fuente básica.")
    except:
        font = ImageFont.load_default()

    # Centrado
    bbox = draw.textbbox((0, 0), text, font=font)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    draw.text(((width - tw) // 2, (height - th) // 2), text, fill=(0, 255, 0), font=font)
    
    path = "ghost_msg.png"
    image.save(path)
    return path