import os
import subprocess
from dotenv import load_dotenv

load_dotenv()

TEMP_DIR = os.getenv("TEMP_DIR", "./temp")
VIDEOS_DIR = os.getenv("VIDEOS_DIR", "./videos")
os.makedirs(VIDEOS_DIR, exist_ok=True)

def create_video():
    output_path = os.path.join(VIDEOS_DIR, f"{generate_filename()}.mp4")

    cmd = [
        "ffmpeg",
        "-y",
        "-f", "concat",
        "-safe", "0",
        "-i", os.path.join(TEMP_DIR, "images_list.txt"),
        "-i", os.path.join(TEMP_DIR, "narration.wav"),
        "-vf", f"ass={os.path.join(TEMP_DIR, 'subtitles.ass')},scale=1280x720",
        "-c:v", "libx264",
        "-preset", "fast",
        "-pix_fmt", "yuv420p",
        "-c:a", "aac",
        "-b:a", "192k",
        output_path
    ]

    subprocess.run(cmd, check=True)
    print(f"[+] Video created successfully: {output_path}")

def generate_filename():
    from datetime import datetime
    now = datetime.now()
    return now.strftime("%Y-%m-%d_%H-%M-%S")

if __name__ == "__main__":
    create_video()

