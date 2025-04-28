from TTS.api import TTS
import os

os.makedirs("./temp", exist_ok=True)

tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=False, gpu=False)
tts.tts_to_file(text="Hello MindBloom, your bot is ready!", file_path="./temp/test_hello.wav")

print("[+] Test audio generated: ./temp/test_hello.wav")
