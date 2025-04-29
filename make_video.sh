#!/bin/bash
# Vai nella cartella principale
cd "$(dirname "$0")"

# Aggiungi la root al PYTHONPATH
export PYTHONPATH=.

echo "[+] Generating text..."
python3 scripts/generate_text.py

echo "[+] Generating audio..."
python3 scripts/generate_audio.py

echo "[+] Downloading images..."
python3 scripts/download_images.py

echo "[+] Creating thumbnail..."
python3 scripts/generate_thumbnail.py

echo "[+] Generating subtitles..."
python3 scripts/generate_subtitles.py

echo "[+] Creating video..."
python3 scripts/create_video.py

echo "[+] Cleaning temp folder..."
python3 scripts/clean_temp.py

echo "[+] Uploading video to YouTube..."
python3 scripts/upload_youtube.py

echo "[+] MindBloom run complete!"

