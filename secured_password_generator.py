"""
Programmer: python_scripts (Abhijith Warrier)

PYTHON SCRIPT TO GENERATE A SECURE PASSWORD USING secrets 🐍🔑🛡️

This script uses Python’s built-in `secrets` module to create cryptographically
secure random passwords.
Unlike `random`, which is predictable, `secrets` is designed for security and
is the recommended way to generate tokens, keys, or passwords.
"""

# Import secrets for secure random generation
import secrets

# Import string to use built-in character sets
import string

# --- Step 1: Define character pool ---
# Combine letters (uppercase + lowercase), digits, and symbols
characters = string.ascii_letters + string.digits + string.punctuation

# --- Step 2: Generate password ---
# Generate a 16-character random password securely
password_length = 16
secure_password = ''.join(secrets.choice(characters) for _ in range(password_length))

# --- Step 3: Display the password ---
print("🔐 Your secure password is:", secure_password)
