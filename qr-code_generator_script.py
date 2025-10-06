"""
Programmer: python_scripts (Abhijith Warrier)

PYTHON SCRIPT TO GENERATE A QR CODE USING qrcode 🐍🧾📱

This script turns any text or URL into a scannable QR code image. You can customize
colors, borders, and sizes easily.

Perfect for sharing project links, contact info, or secrets securely.
"""

# Import the qrcode library to generate QR codes
import qrcode

# --- Step 1: Define the text or URL you want to encode ---
# Replace this link or text with your own content
data = "<YOUR_INPUT_TEXT_FOR_QR_CODE>"

# --- Step 2: Create a QRCode object with configuration ---
# version: controls the size (1 = small, 40 = large)
# error_correction: defines how much of the code can be restored if damaged
# box_size: size of each pixel box in the QR grid
# border: thickness (number of boxes) around the code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# --- Step 3: Add data and build the QR code ---
qr.add_data(data)
qr.make(fit=True)

# --- Step 4: Create an image from the QR code ---
# fill_color sets the QR dots color; back_color sets the background
img = qr.make_image(fill_color="black", back_color="white")

# --- Step 5: Save the QR code image ---
# You can change the filename or format (e.g., .jpg, .bmp)
img.save("<YOUR_QR-CODE_IMAGE_NAME>.png")

print("✅ QR Code generated successfully and saved")
