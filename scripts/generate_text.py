import os
from dotenv import load_dotenv

load_dotenv()

TEMP_DIR = os.getenv("TEMP_DIR", "./temp")
SCRIPT_PATH = os.path.join(TEMP_DIR, "script.txt")
TEXT_PATH = os.path.join(TEMP_DIR, "text.txt")

def generate_text():
    text = """10 Incredible Facts About Space!
1. Some turtles can breathe through their butts.
2. Honey never spoils.
3. Your bones are stronger than steel.
4. There are more stars in the universe than grains of sand on Earth.
5. Humans share 60% of their DNA with bananas.
6. The Eiffel Tower can grow taller in the summer.
7. Octopuses have three hearts.
8. A day on Venus is longer than a year on Venus.
9. Bananas are berries, but strawberries are not.
10. Sharks have been around longer than trees.
Learn more about our incredible world!
Hit like and comment your favorite fact!"""

    # Salva TUTTO il testo nel file script.txt (per l'audio)
    with open(SCRIPT_PATH, "w") as f:
        f.write(text)

    # Salva ogni riga separata nel file text.txt (per i sottotitoli)
    lines = text.split("\n")
    with open(TEXT_PATH, "w") as f:
        for line in lines:
            f.write(line.strip() + "\n")

if __name__ == "__main__":
    generate_text()
    print("[+] Text generated successfully!")

