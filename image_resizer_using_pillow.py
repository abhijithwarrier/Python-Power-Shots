"""
Programmer: python_scripts (Abhijith Warrier)

PYTHON SCRIPT TO COMPRESS OR RESIZE IMAGES USING PILLOW 🐍🖼️⚡

This script compresses images by reducing quality or resizing dimensions.
Perfect for shrinking large PNG/JPG files, optimizing images for web,
or preparing assets for uploads.
"""

# Import Image from Pillow for image processing
from PIL import Image
import os

# --- Step 1: Configure input/output paths ---
INPUT_IMAGE = "input.jpg"          # Replace with your file
OUTPUT_IMAGE = "compressed.jpg"    # Output filename

# --- Step 2: Choose compression settings ---
QUALITY = 40        # Quality level (1–95), lower = smaller size
MAX_WIDTH = 800     # Resize width (keeps aspect ratio)
RESIZE = True       # Set to False to skip resizing

# --- Step 3: Open the image ---
if not os.path.exists(INPUT_IMAGE):
    raise FileNotFoundError(f"Input image not found: {INPUT_IMAGE}")

img = Image.open(INPUT_IMAGE)

# --- Step 4: Resize while maintaining aspect ratio ---
if RESIZE:
    w_percent = MAX_WIDTH / float(img.size[0])
    new_height = int(float(img.size[1]) * w_percent)
    img = img.resize((MAX_WIDTH, new_height), Image.LANCZOS)
    print(f"📐 Resized to: {MAX_WIDTH} x {new_height}px")

# --- Step 5: Save compressed image ---
img.save(
    OUTPUT_IMAGE,
    optimize=True,
    quality=QUALITY
)

print(f"✅ Image compressed and saved as '{OUTPUT_IMAGE}'")
