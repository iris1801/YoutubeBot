import os
import subprocess
from dotenv import load_dotenv

load_dotenv()

TEMP_DIR = os.getenv("TEMP_DIR", "./temp")
OUTPUT_DIR = os.getenv("OUTPUT_DIR", "./videos")
FPS = os.getenv("VIDEO_FPS", "30")
RESOLUTION = os.getenv("VIDEO_RESOLUTION", "1280x720")

def create_video():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    audio = os.path.join(TEMP_DIR, "narration.wav")
    output = os.path.join(OUTPUT_DIR, "final_video.mp4")

    cmd = (
        f"ffmpeg -y -r 1/{FPS} -pattern_type glob -i '{TEMP_DIR}/img_*.jpg' "
        f"-i {audio} -vf scale={RESOLUTION} "
        f"-c:v libx264 -preset veryfast -pix_fmt yuv420p -c:a aac -shortest {output}"
    )
    subprocess.run(cmd, shell=True)

if __name__ == "__main__":
    create_video()