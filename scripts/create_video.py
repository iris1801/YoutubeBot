import os
import subprocess
import wave
import contextlib
from dotenv import load_dotenv

load_dotenv()

TEMP_DIR = os.getenv("TEMP_DIR", "./temp")
OUTPUT_DIR = os.getenv("OUTPUT_DIR", "./videos")
FPS = int(os.getenv("VIDEO_FPS", 30))
RESOLUTION = os.getenv("VIDEO_RESOLUTION", "1280x720")

AUDIO_PATH = os.path.join(TEMP_DIR, "narration.wav")
SUBTITLE_PATH = os.path.join(TEMP_DIR, "subtitles.ass")
VIDEO_OUTPUT = os.path.join(OUTPUT_DIR, f"{subprocess.getoutput('date +%Y-%m-%d_%H-%M-%S')}.mp4")

def get_audio_duration(audio_file):
    with contextlib.closing(wave.open(audio_file, 'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        return frames / float(rate)

def create_video():
    images = sorted([img for img in os.listdir(TEMP_DIR) if img.endswith('.jpg')])
    total_images = len(images)
    audio_duration = get_audio_duration(AUDIO_PATH)
    duration_per_image = audio_duration / total_images

    print(f"[+] Audio duration: {audio_duration:.2f}s, images: {total_images}, each image: {duration_per_image:.2f}s")

    mini_clips = []

    # Creiamo mini-video per ogni immagine
    for idx, img in enumerate(images):
        img_path = os.path.join(TEMP_DIR, img)
        mini_clip = os.path.join(TEMP_DIR, f"clip_{idx}.mp4")
        mini_clips.append(mini_clip)

        subprocess.run([
            "ffmpeg", "-y", "-loop", "1", "-i", img_path,
            "-c:v", "libx264", "-t", f"{duration_per_image:.2f}",
            "-vf", f"scale={RESOLUTION},format=yuv420p",
            mini_clip
        ], check=True)

    # Creiamo file concat_list.txt
    concat_file = os.path.join(TEMP_DIR, "concat_list.txt")
    with open(concat_file, "w") as f:
        for clip in mini_clips:
            f.write(f"file '{clip}'\n")

    # Comando finale per concatenare mini-video con audio e sottotitoli
    cmd = [
        "ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", concat_file,
        "-i", AUDIO_PATH, "-vf", f"ass={SUBTITLE_PATH}",
        "-c:v", "libx264", "-preset", "fast", "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "192k", "-shortest", VIDEO_OUTPUT
    ]

    subprocess.run(cmd, check=True)

    print(f"[+] Video created successfully: {VIDEO_OUTPUT}")

if __name__ == "__main__":
    create_video()
