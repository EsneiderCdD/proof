# mi_proyecto — Descargador de audio (básico)

Breve proyecto para descargar audio de YouTube en formato MP3 usando `yt-dlp` y `ffmpeg`.

## Estructura actual
- `.venv/` — Entorno virtual (local, Windows).
- `downloads/` — Carpeta donde se guardan los MP3 descargados (ya contiene archivos .mp3).
- `downloads_test.py` — Script que solicita una URL de YouTube y descarga/convierte el audio a MP3.
- `links.txt` — Archivo de texto actualmente vacío (posible uso para URLs en lote).
- `README.md` — Documento actual (contiene esta descripción).

## Estado & dependencias
- `yt-dlp` (se utiliza en el script) y `ffmpeg` son necesarios para descargar y convertir audio a MP3.
- `links.txt` está vacío; `downloads/` ya contiene contenido de prueba.
- El script `downloads_test.py` solicita una URL por `input()` y guarda el resultado en `downloads/`.

## Notas rápidas
- El script tiene la creación de carpeta `downloads/` comentada — asegúrate de tener la carpeta si la usas desde cero.
- No se han hecho cambios en archivos fuera de este README; el resto del proyecto se mantiene tal como está.

---
Pequeño y directo: documentación mínima del estado actual del proyecto.

