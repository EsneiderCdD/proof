import os
from yt_dlp import YoutubeDL

OUTPUT_DIR = "downloads"

ydl_opts = {
    "format": "bestaudio/best",              
    "outtmpl": f"{OUTPUT_DIR}/%(title)s.%(ext)s",  
    "postprocessors": [
        {
            "key": "FFmpegExtractAudio",      
            "preferredcodec": "mp3",         
            "preferredquality": "192",       
        }
    ],
}

url = input("Pega aquí el link: ")

with YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

print("\nDescarga completada. Revisa la carpeta 'downloads/'.")
