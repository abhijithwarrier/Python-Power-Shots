"""
Programmer: python_scripts (Abhijith Warrier)

PYTHON SCRIPT TO RENAME MULTIPLE FILES IN A FOLDER AUTOMATICALLY 🐍🗂️🔄

This script loops through all files in a given folder and renames them
using a custom naming pattern.

Perfect for organizing photos, exports, screenshots, or documents quickly.
"""

# Import os to interact with the file system
import os

# --- Step 1: Define the target folder path ---
# Replace this with the path of the folder containing the files you want to rename
folder_path = "<YOUR_FOLDER_PATH_HERE>"

# --- Step 2: Loop through all files in the folder ---
# enumerate() gives both index and filename for easy numbering
for count, filename in enumerate(os.listdir(folder_path), start=1):

    # --- Step 3: Extract file extension to keep the same type (e.g., .png, .txt) ---
    file_ext = os.path.splitext(filename)[1]

    # --- Step 4: Define the new filename pattern ---
    # Example: file_1.png, file_2.png, file_3.png ...
    new_name = f"file_{count}{file_ext}"

    # --- Step 5: Build full paths for renaming ---
    source = os.path.join(folder_path, filename)
    destination = os.path.join(folder_path, new_name)

    # --- Step 6: Rename the file ---
    os.rename(source, destination)

    print(f"✅ Renamed: {filename} → {new_name}")

print("\n🎉 All files have been renamed successfully!")
