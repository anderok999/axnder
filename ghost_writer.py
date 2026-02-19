from PIL import Image, ImageDraw, ImageFont
import os

def create_terminal_message(text):
    # 1. Definimos una resolución Full HD para que la TV no lo vea pequeño
    width, height = 1920, 1080
    
    # Creamos el lienzo negro
    image = Image.new('RGB', (width, height), color='black')
    draw = ImageDraw.Draw(image)
    
    # 2. Sistema inteligente de fuentes (Detección de SO)
    font_path = None
    # Intentamos rutas comunes según el sistema para asegurar texto grueso (Bold)
    possible_fonts = [
        "/system/fonts/Roboto-Bold.ttf",          # Android (Termux)
        "C:\\Windows\\Fonts\\arialbd.ttf",        # Windows
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", # Linux
        "arial.ttf"                               # Fallback
    ]

    for f in possible_fonts:
        if os.path.exists(f):
            font_path = f
            break

    # 3. Ajustamos el tamaño de fuente (Gigante para impacto visual)
    font_size = 180 
    
    try:
        if font_path:
            font = ImageFont.truetype(font_path, font_size)
        else:
            font = ImageFont.load_default()
            print("[!] Advertencia: Usando fuente por defecto (puede verse pequeña).")
    except Exception as e:
        font = ImageFont.load_default()
        print(f"[!] Error cargando fuente: {e}")

    # 4. Centrado dinámico del texto
    # Obtenemos las dimensiones del texto para centrarlo en el lienzo de 1080p
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    x = (width - text_width) // 2
    y = (height - text_height) // 2
    
    # 5. Dibujamos el texto
    # Usamos Verde Neón (Estilo Hacker) para máxima visibilidad
    draw.text((x, y), text, fill=(0, 255, 65), font=font)
    
    # Guardamos el payload visual
    output_path = "ghost_msg.png"
    image.save(output_path)
    
    return output_path