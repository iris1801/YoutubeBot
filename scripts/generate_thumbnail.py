import os
from dotenv import load_dotenv
from PIL import Image, ImageDraw, ImageFont, ImageFilter

load_dotenv()

TEMP_DIR = os.getenv("TEMP_DIR", "./temp")

def create_thumbnail(title):
    img_path = os.path.join(TEMP_DIR, "img_0.jpg")
    thumb_path = os.path.join(TEMP_DIR, "thumbnail.jpg")

    base = Image.open(img_path).resize((1280, 720))
    blurred = base.filter(ImageFilter.GaussianBlur(radius=5))

    draw = ImageDraw.Draw(blurred)
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 64)

    text_width, text_height = draw.textsize(title, font=font)

    x = (1280 - text_width) / 2
    y = (720 - text_height) / 2

    # Black transparent rectangle
    draw.rectangle(((0, y-20), (1280, y + text_height + 20)), fill=(0, 0, 0, 180))

    draw.text((x, y), title, font=font, fill=(255, 255, 255))

    blurred.save(thumb_path)

if __name__ == "__main__":
    with open(os.path.join(TEMP_DIR, "script.txt"), "r") as f:
        title = f.readline().strip()
    create_thumbnail(title)