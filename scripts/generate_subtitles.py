import os
from dotenv import load_dotenv
import whisper

load_dotenv()

TEMP_DIR = os.getenv("TEMP_DIR", "./temp")

def generate_subtitles():
    model = whisper.load_model("small")
    audio_path = os.path.join(TEMP_DIR, "narration.wav")
    result = model.transcribe(audio_path)
    srt_path = os.path.join(TEMP_DIR, "subtitles.srt")
    with open(srt_path, "w") as srt:
        srt.write(result['text'])

if __name__ == "__main__":
    generate_subtitles()