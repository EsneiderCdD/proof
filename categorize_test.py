import os
import json
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("❌ ERROR: Falta GEMINI_API_KEY en tu archivo .env")

client = genai.Client(api_key=api_key)

TRANSCRIPTS_DIR = "downloads"
MODEL_NAME = "gemini-2.0-flash"

def build_prompt(transcript_text: str):
    return f"""
Analiza la siguiente transcripción corta de un reel/short.

- Responde SOLO con un JSON puro.
- NO coloques nada fuera del JSON (ni ```json, ni explicación).
- No inventes datos.
- Si no existe un dato, déjalo como "".
- La descripción corta debe tener máximo 1 frase breve.
- La descripción larga puede tener más detalle pero sin adornos.
- Si hay website real mencionado, inclúyelo; si no, "".

{{
  "titulo": "",
  "descripcion_corta": "",
  "descripcion_larga": "",
  "website": ""
}}

{transcript_text}
"""

def extract_json(text: str):
    """
    Elimina bloques ```json, ``` y cualquier texto basura
    dejando solo el JSON.
    """

    text = text.strip()

    if "```" in text:
        text = text.replace("```json", "").replace("```", "").strip()

    if "{" in text and "}" in text:
        start = text.find("{")
        end = text.rfind("}") + 1
        text = text[start:end]

    return text

def list_text_files():
    return [f for f in os.listdir(TRANSCRIPTS_DIR) if f.endswith(".txt")]

def main():

    print("\n=== Archivos disponibles en downloads/ ===")
    text_files = list_text_files()

    if not text_files:
        print("❌ No hay archivos .txt para procesar.")
        return

    for i, file in enumerate(text_files):
        print(f"{i + 1}. {file}")

    index = int(input("\nSelecciona el archivo por número: ")) - 1

    if index < 0 or index >= len(text_files):
        print("❌ Selección inválida")
        return

    selected_file = text_files[index]
    file_path = os.path.join(TRANSCRIPTS_DIR, selected_file)

    print(f"\nProcesando → {selected_file}\n")

    with open(file_path, "r", encoding="utf-8") as f:
        transcript = f.read()

    prompt = build_prompt(transcript)

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )

    raw_output = response.text
    print("\n=== Respuesta del modelo (cruda) ===\n")
    print(raw_output)

    cleaned_json = extract_json(raw_output)

    output_file = selected_file.replace(".txt", "_categorized.json")
    output_path = os.path.join(TRANSCRIPTS_DIR, output_file)

    try:
        parsed = json.loads(cleaned_json)

        with open(output_path, "w", encoding="utf-8") as out:
            json.dump(parsed, out, ensure_ascii=False, indent=4)

        print(f"\n✅ JSON válido guardado en: {output_file}")

    except json.JSONDecodeError:
        print("\n⚠️ ERROR: Gemini no devolvió JSON válido incluso después de limpiar.")
        print("   Puedes editar a mano o reenviar la transcripción.")

if __name__ == "__main__":
    main()
