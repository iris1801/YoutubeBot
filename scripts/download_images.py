import os
from dotenv import load_dotenv
from pexels_api import API

load_dotenv()

PEXELS_API_KEY = os.getenv("PEXELS_API_KEY")
TEMP_DIR = os.getenv("TEMP_DIR", "./temp")
NUMBER_OF_IMAGES = int(os.getenv("NUMBER_OF_IMAGES", 7))

def download_images(query="science"):
    api = API(PEXELS_API_KEY)
    api.search(query, page=1, results_per_page=NUMBER_OF_IMAGES)
    photos = api.get_entries()

    os.makedirs(TEMP_DIR, exist_ok=True)

    for idx, photo in enumerate(photos):
        url = photo.original
        os.system(f"wget -O {TEMP_DIR}/img_{idx}.jpg {url}")

if __name__ == "__main__":
    download_images()