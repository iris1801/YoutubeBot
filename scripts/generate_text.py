import os
from dotenv import load_dotenv
from scripts.utils.seo_generator import generate_seo_title_and_description

load_dotenv()

OUTPUT_DIR = os.getenv("TEMP_DIR", "./temp")

def generate_curiosities():
    curiosities = []
    for i in range(1, 11):
        curiosities.append(f"{i}. {fake_curiosity()}")
    return curiosities

def fake_curiosity():
    # Funzione finta da rimpiazzare con modello AI locale (LLaMA, GPT4All ecc.)
    # Qui puoi integrare GPT se vuoi poi migliorarla
    import random
    topics = [
        "Sharks have been around longer than trees.",
        "Bananas are berries, but strawberries are not.",
        "Octopuses have three hearts.",
        "Honey never spoils.",
        "Humans share 60% of their DNA with bananas.",
        "The Eiffel Tower can grow taller in the summer.",
        "Some turtles can breathe through their butts.",
        "There are more stars in the universe than grains of sand on Earth.",
        "A day on Venus is longer than a year on Venus.",
        "Your bones are stronger than steel."
    ]
    return random.choice(topics)

def save_script(title, curiosities, description):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(os.path.join(OUTPUT_DIR, "script.txt"), "w") as f:
        f.write(title + "\n\n")
        for curiosity in curiosities:
            f.write(curiosity + "\n")
        f.write("\n" + description)

if __name__ == "__main__":
    title, description = generate_seo_title_and_description()
    curiosities = generate_curiosities()
    save_script(title, curiosities, description)