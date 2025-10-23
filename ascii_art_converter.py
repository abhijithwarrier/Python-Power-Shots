"""
Programmer: python_scripts (Abhijith Warrier)

PYTHON SCRIPT TO CONVERT AN IMAGE INTO ASCII ART 🐍🖼️➡️🔡

This script loads an image, resizes it for terminal-friendly proportions,
maps pixel brightness to ASCII characters, and prints/saves the result.
Perfect for creative visuals, terminal art, or fun profile banners.
"""

# Import PIL for image loading and processing
from PIL import Image

# Import os for optional path handling
import os

# --- Configuration you can tweak ---
IMAGE_PATH = "input.jpg"   # <-- Change this to your image path (PNG/JPG)
OUTPUT_TXT = "ascii_art.txt"  # Set to None to skip saving to file
TERMINAL_WIDTH = 100       # Target text width (characters)
INVERT = False             # True = dark chars on light areas; False = normal mapping

# ASCII ramp from dark (index 0) to light (last index).
# You can try denser ramps for more detail.
ASCII_CHARS = "@%#*+=-:. "  # 10 levels; swap order or use reversed for invert


def image_to_ascii(image_path: str,
                   width: int = 100,
                   invert: bool = False,
                   charset: str = ASCII_CHARS) -> str:
    """
    Convert an image to ASCII art and return it as a multi-line string.

    Args:
        image_path: Path to input image (JPG/PNG).
        width: Output character width (height is auto-calculated).
        invert: If True, flips the brightness mapping.
        charset: Characters from darkest -> lightest.

    Returns:
        A string containing the ASCII art (lines separated by '\n').
    """
    # 1) Load image and convert to grayscale
    img = Image.open(image_path).convert("L")  # "L" = 8-bit grayscale

    # 2) Compute resized dimensions.
    # Terminal text cells are taller than they are wide, so we correct aspect ratio.
    # The factor ~0.45 works well for many monospace fonts.
    orig_w, orig_h = img.size
    aspect_ratio = orig_h / orig_w
    new_w = max(10, int(width))
    new_h = max(5, int(aspect_ratio * new_w * 0.45))

    img = img.resize((new_w, new_h))

    # 3) Optionally invert the character ramp
    chars = charset[::-1] if invert else charset
    n = len(chars)

    # 4) Map each pixel (0-255) to a character index
    # index = pixel/255 * (n-1), rounded down
    pixels = img.getdata()
    mapped = [chars[int(p / 255 * (n - 1))] for p in pixels]

    # 5) Join rows
    lines = ["".join(mapped[i:i + new_w]) for i in range(0, len(mapped), new_w)]
    return "\n".join(lines)


def main():
    # Validate source image path
    if not os.path.exists(IMAGE_PATH):
        raise FileNotFoundError(f"Input image not found: {IMAGE_PATH}")

    ascii_art = image_to_ascii(
        image_path=IMAGE_PATH,
        width=TERMINAL_WIDTH,
        invert=INVERT,
        charset=ASCII_CHARS
    )

    # Print to terminal
    print(ascii_art)

    # Optionally save to a text file
    if OUTPUT_TXT:
        with open(OUTPUT_TXT, "w", encoding="utf-8") as f:
            f.write(ascii_art)
        print(f"\n✅ ASCII art saved to: {OUTPUT_TXT}")


if __name__ == "__main__":
    main()
