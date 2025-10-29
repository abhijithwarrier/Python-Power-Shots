"""
Programmer: python_scripts (Abhijith Warrier)

PYTHON SCRIPT TO COPY AND PASTE TEXT USING pyperclip 🐍📋⚡

This script demonstrates how to interact with your system clipboard —
copying text into it or reading text from it — using the pyperclip library.
Perfect for quick automation, utilities, or workflow helpers.
"""

# Import pyperclip for clipboard access
import pyperclip

# --- Step 1: Copy text to clipboard ---
text_to_copy = "Python Power Shots – Tiny scripts, big power!"
pyperclip.copy(text_to_copy)
print(f"✅ Text copied to clipboard:\n{text_to_copy}\n")

# --- Step 2: Paste (retrieve) the clipboard content ---
clipboard_content = pyperclip.paste()
print(f"📋 Clipboard currently contains:\n{clipboard_content}")

# --- Tip: Combine this with other scripts ---
# For example, automatically copy generated passwords, links, or summaries.