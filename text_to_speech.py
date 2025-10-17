"""
Programmer: python_scripts (Abhijith Warrier)

PYTHON SCRIPT TO MAKE PYTHON SPEAK USING pyttsx3 🐍🗣️🎧

This script uses the pyttsx3 library to convert text into speech.
It works offline and lets you customize the voice, rate, and volume.
Perfect for accessibility tools, assistants, or interactive scripts.
"""

# Import pyttsx3 for text-to-speech conversion
import pyttsx3

# --- Step 1: Initialize the text-to-speech engine ---
engine = pyttsx3.init()

# --- Step 2: Set properties for the voice ---
# Adjust speaking rate (default is ~200 words per minute)
engine.setProperty('rate', 175)

# Adjust volume (range: 0.0 to 1.0)
engine.setProperty('volume', 0.9)

# Get available voices and set one (0 = male, 1 = female)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # use female voice; change to voices[0] for male

# --- Step 3: Define text to speak ---
text = "Hello there! Python can speak too."

# --- Step 4: Make Python speak the text ---
engine.say(text)

# --- Step 5: Block while speaking (wait until done) ---
engine.runAndWait()

print("✅ Python has spoken successfully!")
