# mi_proyecto — Knowledge Collector (ETL / Audio Processing Pipeline)

Proyecto ETL sencillo para extraer audio de YouTube, transcribirlo y generar metadatos categorizados.
Usa `yt-dlp` y `ffmpeg` para la extracción, `whisper` para transcripción y Gemini (`google-genai`) para clasificación.

## Estructura actual
- `.venv/` — Entorno virtual (local, Windows).
- `downloads/` — Carpeta donde se guardan los MP3 descargados (ya contiene archivos .mp3).
- `downloads_test.py` — Script que solicita una URL de YouTube y descarga/convierte el audio a MP3.
- `links.txt` — Archivo de texto actualmente vacío (posible uso para URLs en lote).
- `README.md` — Documento actual (contiene esta descripción).
- `transcribe_test.py` — Script que lista los MP3 en `downloads/`, permite seleccionar uno y transcribe a texto usando `whisper`.
 - `categorize_test.py` — Script que procesa transcripciones (.txt) con Gemini (Google GenAI) para generar un JSON categorizado (guarda *_categorized.json en `downloads/`).

## Estado & dependencias
- `yt-dlp` (se utiliza en el script) y `ffmpeg` son necesarios para descargar y convertir audio a MP3.
- `whisper` (la librería para transcripción) es necesaria para que `transcribe_test.py` funcione.
- `python-dotenv` y la librería de Gemini (`google-genai` o similar) son necesarias para `categorize_test.py`.
- `links.txt` está vacío; `downloads/` ya contiene contenido de prueba.
- El script `downloads_test.py` solicita una URL por `input()` y guarda el resultado en `downloads/`.
 - El script `transcribe_test.py` muestra los MP3 en `downloads/`, pide seleccionar uno y guarda la transcripción como un archivo .txt junto al MP3.
 - El script `categorize_test.py` lee transcripciones .txt desde `downloads/`, construye un prompt y llama a Gemini para generar un JSON con título/descripcion/website; se requiere la variable `GEMINI_API_KEY` en un archivo `.env`.

## Notas rápidas
- El script tiene la creación de carpeta `downloads/` comentada — asegúrate de tener la carpeta si la usas desde cero.
- No se han hecho cambios en archivos fuera de este README; el resto del proyecto se mantiene tal como está.

---
Pequeño y directo: documentación mínima del estado actual del proyecto.

