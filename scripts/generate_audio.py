import os
import re
from TTS.api import TTS
from dotenv import load_dotenv

# Carica variabili d'ambiente da .env
load_dotenv()

# Percorsi dei file e delle cartelle
TEMP_DIR = os.getenv("TEMP_DIR", "./temp")
AUDIO_PATH = os.path.join(TEMP_DIR, "narration.wav")
TEXT_PATH = os.path.join(TEMP_DIR, "script.txt")

# Inizializza il motore di sintesi vocale
tts = TTS(model_name=os.getenv("COQUI_VOICE_NAME"))

# Funzione per rimuovere le emoji dal testo
def clean_text(text):
    emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticon
        u"\U0001F300-\U0001F5FF"  # simboli vari
        u"\U0001F680-\U0001F6FF"  # trasporti/mappe
        u"\U0001F1E0-\U0001F1FF"  # bandiere
        u"\U00002700-\U000027BF"  # Dingbats
        u"\U000024C2-\U0001F251"  # altri simboli
        "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', text)

# Funzione principale per generare l'audio
def generate_audio(text_file):
    # Legge il file di testo riga per riga
    with open(text_file, "r") as f:
        lines = f.readlines()
    
    # Pulisce e filtra le righe
    lines = [clean_text(line.strip()) for line in lines if len(line.strip().split()) > 2]

    # Combina tutte le linee filtrate in un unico testo
    text = " ".join(lines)

    # Verifica che il testo finale non sia vuoto
    if not text.strip():
        raise ValueError("Errore: il testo da leggere è vuoto dopo la pulizia!")

    # Sintetizza l'audio e salva il file
    tts.tts_to_file(text=text, file_path=AUDIO_PATH)

if __name__ == "__main__":
    generate_audio(TEXT_PATH)
    print("[+] Audio generated successfully!")

