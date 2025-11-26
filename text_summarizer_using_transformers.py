"""
Programmer: python_scripts (Abhijith Warrier)

PYTHON SCRIPT TO GENERATE QUICK TEXT SUMMARIES USING transformers 🐍📝⚡

This script uses Hugging Face's transformers library to summarize large text
blocks into short, meaningful summaries. Perfect for condensing articles,
reports, notes, or any long content.
"""

# Import the summarization pipeline from transformers
from transformers import pipeline

# --- Step 1: Load the summarization model ---
# 'facebook/bart-large-cnn' is a popular, high-quality summarization model.
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# --- Step 2: Provide the text you want to summarize ---
text = """
Python is a versatile programming language widely used for web development,
data science, machine learning, automation, and more. Its clean syntax and
extensive library ecosystem make it a favorite among developers. With the rise
of AI and data-driven applications, Python has become one of the most important
languages in the tech world.
"""

# --- Step 3: Generate the summary ---
summary = summarizer(
    text,
    max_length=60,   # Maximum length of summary
    min_length=20,   # Minimum acceptable length
    do_sample=False  # Deterministic output
)

# --- Step 4: Print the summary ---
print("🔍 SUMMARY:\n")
print(summary[0]["summary_text"])