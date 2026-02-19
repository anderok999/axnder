from PIL import Image, ImageDraw, ImageFont
import os

def create_terminal_message(text, filename="ghost_msg.png"):
    # Tamaño estándar Full HD
    width, height = 1920, 1080
    background_color = (0, 0, 0) # Negro
    text_color = (0, 255, 255) # Cian Neón
    
    # Crear lienzo
    img = Image.new('RGB', (width, height), color=background_color)
    d = ImageDraw.Draw(img)
    
    # Intentar cargar una fuente monoespaciada (estilo terminal)
    try:
        # En Windows suele estar esta:
        font = ImageFont.truetype("lucon.ttf", 80) 
    except:
        font = ImageFont.load_default()

    # Dibujar encabezado estilo AXNDER
    d.text((100, 100), ">>> AXNDER REMOTE TERMINAL OVERRIDE <<<", fill=(0, 255, 0), font=font)
    d.text((100, 180), "---------------------------------------", fill=(0, 255, 255), font=font)
    
    # Dibujar el mensaje del usuario
    d.text((150, 450), f"> {text}", fill=text_color, font=font)
    
    # Dibujar pie de página
    d.text((100, 900), "STATUS: INJECTED VIA RNIBO PROTOCOL", fill=(255, 0, 0), font=font)

    img.save(filename)
    return filename