import os
import shutil
from dotenv import load_dotenv

load_dotenv()

TEMP_DIR = os.getenv("TEMP_DIR", "./temp")

def clean_temp_folder():
    for filename in os.listdir(TEMP_DIR):
        file_path = os.path.join(TEMP_DIR, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f"[!] Failed to delete {file_path}. Reason: {e}")

if __name__ == "__main__":
    clean_temp_folder()
    print("[+] Temp folder cleaned successfully!")

