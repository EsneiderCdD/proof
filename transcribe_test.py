import os
import whisper

# 1. Carpeta donde están los audios descargados
AUDIO_DIR = "downloads"

# 2. Cargar el modelo de Whisper
#    "base" es rápido y suficientemente bueno para pruebas.
model = whisper.load_model("base")

# 3. Mostrar archivos disponibles
files = [f for f in os.listdir(AUDIO_DIR) if f.endswith(".mp3")]

if not files:
    print("No hay archivos MP3 en la carpeta 'downloads/'. Descarga uno primero.")
    exit()

print("Audios disponibles:")
for i, f in enumerate(files, start=1):
    print(f"{i}. {f}")

# 4. Preguntar cuál transcribir
choice = int(input("\nSelecciona el número del audio a transcribir: ")) - 1
audio_path = os.path.join(AUDIO_DIR, files[choice])

print(f"\nTranscribiendo: {audio_path} ...\n")

# 5. Transcribir
result = model.transcribe(audio_path)

# 6. Guardar en .txt con el mismo nombre que el mp3
txt_path = audio_path.replace(".mp3", ".txt")

with open(txt_path, "w", encoding="utf-8") as f:
    f.write(result["text"])

print(f"Transcripción completada.\nArchivo guardado en:\n{txt_path}")
