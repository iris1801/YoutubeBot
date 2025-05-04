import os
import random
import requests
from dotenv import load_dotenv

load_dotenv()

PEXELS_API_KEY = os.getenv("PEXELS_API_KEY")
NUMBER_OF_IMAGES = int(os.getenv("NUMBER_OF_IMAGES", 13))
TEMP_DIR = os.getenv("TEMP_DIR", "./temp")
PEXELS_IMAGE_QUALITY = os.getenv("PEXELS_IMAGE_QUALITY", "original")

HEADERS = {
    "Authorization": PEXELS_API_KEY
}

def search_images(query, per_page=80):
    url = f"https://api.pexels.com/v1/search?query={query}&per_page={per_page}"
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        return response.json()["photos"]
    else:
        print(f"[-] Error searching images: {response.status_code} {response.text}")
        return []

def download_images():
    os.makedirs(TEMP_DIR, exist_ok=True)

    with open(os.path.join(TEMP_DIR, "script.txt"), "r") as f:
        lines = [line.strip() for line in f if line.strip()]

    if not lines:
        print("[-] No text lines found to search images.")
        return

    search_query = " ".join(lines[0].split()[:3])  # primi 3 vocaboli per cercare
    photos = search_images(search_query)

    if not photos:
        print("[-] No images found, trying a fallback search for 'nature'")
        photos = search_images("nature")  # fallback a qualcosa di generico

    if not photos:
        print("[-] Still no images found, aborting.")
        return

    selected_photos = random.sample(photos, min(NUMBER_OF_IMAGES, len(photos)))

    with open(os.path.join(TEMP_DIR, "images_list.txt"), "w") as f_list:
        for idx, photo in enumerate(selected_photos):
            img_url = photo["src"].get(PEXELS_IMAGE_QUALITY) or photo["src"]["original"]
            img_path = os.path.join(TEMP_DIR, f"img_{idx}.jpg")
            try:
                img_data = requests.get(img_url).content
                with open(img_path, "wb") as handler:
                    handler.write(img_data)
                f_list.write(f"file '{img_path}'\n")
            except Exception as e:
                print(f"[-] Failed to download image {idx}: {e}")

    print("[+] Images downloaded and images_list.txt created successfully!")

if __name__ == "__main__":
    download_images()
