#!/bin/bash

source /youtube_bot/.env

echo "[+] Generating text..."
python3 scripts/generate_text.py

echo "[+] Generating audio..."
python3 scripts/generate_audio.py

echo "[+] Downloading images..."
python3 scripts/download_images.py

echo "[+] Creating thumbnail..."
python3 scripts/generate_thumbnail.py

echo "[+] Creating video..."
python3 scripts/create_video.py

echo "[+] Generating subtitles..."
python3 scripts/generate_subtitles.py

echo "[+] Uploading video to YouTube..."
python3 scripts/upload_video.py

echo "[+] MindBloom run complete!"