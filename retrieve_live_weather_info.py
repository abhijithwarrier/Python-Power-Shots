"""
Programmer: python_scripts (Abhijith Warrier)

PYTHON SCRIPT TO GET LIVE WEATHER INFO USING A PUBLIC API 🐍🌤️🌍

This script fetches real-time weather details from wttr.in using a
simple GET request — no API key required.
Perfect for terminal dashboards, automation, or quick lookups.
"""

# Import requests to make HTTP requests
import requests

# --- Step 1: Define the city you want weather info for ---
city = "Pune"  # You can replace this with any city name

# --- Step 2: Fetch weather data from wttr.in ---
url = f"https://wttr.in/{city}?format=j1"
response = requests.get(url)

# --- Step 3: Check if the request was successful ---
if response.status_code == 200:
    data = response.json()

    # --- Step 4: Extract useful information ---
    current = data["current_condition"][0]
    temperature = current["temp_C"]
    feels_like = current["FeelsLikeC"]
    humidity = current["humidity"]
    weather_desc = current["weatherDesc"][0]["value"]

    # --- Step 5: Display the weather report ---
    print(f"🌍 Weather in {city}:")
    print(f"🌡️ Temperature: {temperature}°C (Feels like {feels_like}°C)")
    print(f"💧 Humidity: {humidity}%")
    print(f"☁️ Condition: {weather_desc}")

else:
    print("⚠️ Failed to fetch weather data. Please check your city name or internet connection.")
