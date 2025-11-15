"""
Programmer: python_scripts (Abhijith Warrier)

PYTHON SCRIPT TO AUTO-ORGANIZE FILES BY EXTENSION OR DATE 🐍🗃️📂

This script scans a target folder and moves files into subfolders based on
either their file extension (e.g., png, pdf, txt) or their last modified date
(e.g., 2025-11-15). Perfect for cleaning up Downloads or Desktop quickly.
"""

from pathlib import Path
import shutil
from datetime import datetime

# --- Configuration you can tweak ---

# Folder whose files you want to organize
TARGET_FOLDER = Path("<MENTION_YOUR_FOLDER_PATH>")

# Organize mode: "extension" or "date"
ORGANIZE_BY = "extension"  # or "date"

# If True, print what is happening; set False for silent mode
VERBOSE = True


def get_extension_folder(file_path: Path) -> str:
    """
    Return a folder name based on file extension.
    Example: 'image.png' -> 'png'
    If no extension, use 'no_extension'.
    """
    ext = file_path.suffix.lower().lstrip(".")
    return ext if ext else "no_extension"


def get_date_folder(file_path: Path) -> str:
    """
    Return a folder name based on last modified date.
    Example: 2025-11-15
    """
    mtime = file_path.stat().st_mtime
    dt = datetime.fromtimestamp(mtime)
    return dt.strftime("%Y-%m-%d")


def organize_files(folder: Path, mode: str = "extension") -> None:
    """
    Organize files in 'folder' by the given mode:
    - "extension": group by file extension
    - "date": group by last modified date
    """
    if not folder.exists() or not folder.is_dir():
        raise NotADirectoryError(f"Target folder does not exist or is not a directory: {folder}")

    for item in folder.iterdir():
        # Skip directories (only process files)
        if item.is_dir():
            continue

        # Choose destination folder name based on mode
        if mode == "extension":
            dest_folder_name = get_extension_folder(item)
        elif mode == "date":
            dest_folder_name = get_date_folder(item)
        else:
            raise ValueError("ORGANIZE_BY must be 'extension' or 'date'")

        dest_folder = folder / dest_folder_name

        # Create destination folder if it doesn't exist
        dest_folder.mkdir(exist_ok=True)

        # Build full destination path (same filename, new folder)
        dest_path = dest_folder / item.name

        # Move the file
        shutil.move(str(item), str(dest_path))

        if VERBOSE:
            print(f"✅ Moved: {item.name}  →  {dest_folder_name}/")


def main():
    print(f"📂 Organizing files in: {TARGET_FOLDER}")
    print(f"📁 Mode: {ORGANIZE_BY!r}\n")

    organize_files(TARGET_FOLDER, ORGANIZE_BY)

    print("\n🎉 File organization complete!")


if __name__ == "__main__":
    main()
