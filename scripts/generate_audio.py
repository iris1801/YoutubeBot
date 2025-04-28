import os
from dotenv import load_dotenv
import coqui_tts

load_dotenv()

TEMP_DIR = os.getenv("TEMP_DIR", "./temp")
VOICE_NAME = os.getenv("COQUI_VOICE_NAME", "female-english")

def generate_audio(text_file):
    with open(text_file, "r") as f:
        text = f.read()
    tts = coqui_tts.TTS(VOICE_NAME)
    audio_path = os.path.join(TEMP_DIR, "narration.wav")
    tts.tts_to_file(text=text, file_path=audio_path)

if __name__ == "__main__":
    generate_audio(os.path.join(TEMP_DIR, "script.txt"))