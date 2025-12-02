import os
from yt_dlp import YoutubeDL

# 1. Ruta donde guardaremos los audios
OUTPUT_DIR = "downloads"

# 2. Si la carpeta no existe, la creamos
# if not os.path.exists(OUTPUT_DIR):
#     os.makedirs(OUTPUT_DIR)

# 3. Configuración de yt-dlp
ydl_opts = {
    "format": "bestaudio/best",                # mejor calidad de audio posible
    "outtmpl": f"{OUTPUT_DIR}/%(title)s.%(ext)s",   # cómo se guardará el archivo
    "postprocessors": [
        {
            "key": "FFmpegExtractAudio",       # usa ffmpeg
            "preferredcodec": "mp3",           # queremos mp3
            "preferredquality": "192",         # calidad estándar
        }
    ],
}

# 4. Pedimos al usuario un link
url = input("Pega aquí el link de YouTube: ")

# 5. Ejecutamos la descarga
with YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

print("\nDescarga completada. Revisa la carpeta 'downloads/'.")
