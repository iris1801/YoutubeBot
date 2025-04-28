#!/bin/bash

echo "[+] Installing OpenVoice TTS dependencies..."
sudo apt update
sudo apt install -y python3-pip ffmpeg
pip3 install TTS==0.15.1 torch torchvision torchaudio
echo "[+] OpenVoice TTS installed successfully."