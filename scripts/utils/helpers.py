import os
from dotenv import load_dotenv

load_dotenv()

def load_env():
    return {
        "PEXELS_API_KEY": os.getenv("PEXELS_API_KEY"),
        "TEMP_DIR": os.getenv("TEMP_DIR", "./temp"),
        "OUTPUT_DIR": os.getenv("OUTPUT_DIR", "./videos")
    }