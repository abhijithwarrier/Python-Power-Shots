"""
Programmer: python_scripts (Abhijith Warrier)

PYTHON SCRIPT TO CAPTURE A WEBPAGE SCREENSHOT USING SELENIUM 🐍🌐📸

This script opens a webpage in a headless Chrome browser and saves
a screenshot as an image. Useful for UI monitoring, reports, or
automated documentation.
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# --- Step 1: Configure Chrome options ---
chrome_options = Options()
chrome_options.add_argument("--headless")          # Run without UI
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("--disable-gpu")

# --- Step 2: Set ChromeDriver path ---
# Make sure chromedriver is installed and matches your Chrome version
CHROMEDRIVER_PATH = "/usr/local/bin/chromedriver"  # Update if needed

service = Service(CHROMEDRIVER_PATH)
driver = webdriver.Chrome(service=service, options=chrome_options)

# --- Step 3: Open the target webpage ---
url = "https://awdevrethought.com"
driver.get(url)

# Give the page time to load
time.sleep(3)

# --- Step 4: Capture screenshot ---
output_file = "awdevrethought_screenshot.png"
driver.save_screenshot(output_file)

print(f"📸 Screenshot saved as '{output_file}'")

# --- Step 5: Close the browser ---
driver.quit()