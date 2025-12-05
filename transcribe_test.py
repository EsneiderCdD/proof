import os
import whisper

AUDIO_DIR = "downloads"

model = whisper.load_model("base")

files = [f for f in os.listdir(AUDIO_DIR) if f.endswith(".mp3")]

if not files:
    print("No hay archivos MP3 en la carpeta 'downloads/'. Descarga uno primero.")
    exit()

print("Audios disponibles:")
for i, f in enumerate(files, start=1):
    print(f"{i}. {f}")

choice = int(input("\nSelecciona el número del audio a transcribir: ")) - 1
audio_path = os.path.join(AUDIO_DIR, files[choice])

print(f"\nTranscribiendo: {audio_path} ...\n")

result = model.transcribe(audio_path)

txt_path = audio_path.replace(".mp3", ".txt")

with open(txt_path, "w", encoding="utf-8") as f:
    f.write(result["text"])

print(f"Transcripción completada.\nArchivo guardado en:\n{txt_path}")
