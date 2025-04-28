#!/bin/bash

echo "[+] Updating system..."
sudo apt update

echo "[+] Installing necessary packages..."
sudo apt install -y python3 python3-pip ffmpeg git

echo "[+] Installing Python requirements..."
pip3 install -r requirements.txt

echo "[+] All done!"