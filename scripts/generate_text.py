import os
import random
import requests
from dotenv import load_dotenv

load_dotenv()

# Caricamento delle variabili di ambiente
TEMP_DIR = os.getenv("TEMP_DIR", "./temp")
TEXT_PATH = os.path.join(TEMP_DIR, "script.txt")
OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://localhost:11434")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "phi")
THEMES = os.getenv("THEMES", "space,chemistry,biology,technology,artificial intelligence").split(",")

os.makedirs(TEMP_DIR, exist_ok=True)

def generate_prompt(theme):
    prompt = (
        f"Generate a Top 10 list of amazing fun facts about {theme}.\n"
        "Each fact must be 1 or 2 sentences maximum.\n"
        "Only return the list, with each fact starting with its number followed by a dot.\n"
        "No extra introductions or conclusions, no titles.\n"
        "Everything must be in fluent and correct English."
    )
    return prompt

def generate_text():
    theme = random.choice(THEMES)
    prompt = generate_prompt(theme)
    
    print(f"[+] Selected theme: {theme}")

    response = requests.post(
        f"{OLLAMA_HOST}/api/generate",
        json={
            "model": OLLAMA_MODEL,
            "prompt": prompt,
            "stream": False,
        },
    )

    if response.status_code != 200:
        print("[-] Error generating text with Ollama.")
        print(response.text)
        exit(1)

    result = response.json()
    text = result.get("response", "").strip()

    if not text:
        print("[-] No text generated!")
        exit(1)

    with open(TEXT_PATH, "w", encoding="utf-8") as f:
        f.write(text)

    print("[+] Text generated and saved successfully!")

if __name__ == "__main__":
    generate_text()
