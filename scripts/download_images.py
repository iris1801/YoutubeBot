import os
import requests
import random
from dotenv import load_dotenv

load_dotenv()

TEMP_DIR = os.getenv("TEMP_DIR", "./temp")
PEXELS_API_KEY = os.getenv("PEXELS_API_KEY")
NUM_IMAGES = 13  # numero immagini = numero frasi

PEXELS_SEARCH_QUERY = "space"  # qui puoi cambiarlo se vuoi (es: "universe", "galaxy")

def download_images():
    if not PEXELS_API_KEY:
        raise ValueError("PEXELS_API_KEY mancante nel .env!")

    os.makedirs(TEMP_DIR, exist_ok=True)

    headers = {
        "Authorization": PEXELS_API_KEY
    }

    response = requests.get(
        f"https://api.pexels.com/v1/search?query={PEXELS_SEARCH_QUERY}&per_page=30",
        headers=headers,
        timeout=10
    )

    if response.status_code != 200:
        raise Exception(f"Errore Pexels API: {response.status_code} - {response.text}")

    data = response.json()
    photos = data.get("photos", [])

    if len(photos) < NUM_IMAGES:
        raise Exception(f"Non ci sono abbastanza immagini su Pexels per '{PEXELS_SEARCH_QUERY}' (trovate: {len(photos)})")

    selected_photos = random.sample(photos, NUM_IMAGES)

    images_list_path = os.path.join(TEMP_DIR, "images_list.txt")
    with open(images_list_path, "w") as list_file:
        for idx, photo in enumerate(selected_photos):
            img_url = photo["src"]["landscape"]  # 1280x720-ish proporzioni
            img_path = os.path.join(TEMP_DIR, f"img_{idx:03d}.jpg")

            try:
                img_data = requests.get(img_url, timeout=10).content
                with open(img_path, "wb") as f:
                    f.write(img_data)
                print(f"[+] Downloaded {img_path}")
                list_file.write(f"file '{img_path}'\n")
                list_file.write("duration 3\n")
            except Exception as e:
                print(f"[-] Errore scaricando immagine {idx}: {e}")
                raise SystemExit("[X] Fatal: Errore durante il download immagini.")

        # Duplichiamo ultima immagine senza durata per chiudere bene il video
        list_file.write(f"file '{img_path}'\n")

if __name__ == "__main__":
    download_images()
    print("[+] Immagini scaricate da Pexels e images_list.txt creato con successo!")

