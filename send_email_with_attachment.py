"""
Programmer: python_scripts (Abhijith Warrier)

PYTHON SCRIPT TO SEND EMAILS WITH ATTACHMENTS USING smtplib 🐍📧📎

This script sends an email with a subject, body, and file attachment using Python's
built-in smtplib and email libraries.
Perfect for automating reports, logs, documents, or notifications.
"""

# Import smtplib to send emails
import smtplib

# Import email modules to construct MIME messages
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# --- Step 1: Email account configuration ---
sender_email = "your_email@example.com"
sender_password = "YOUR_PASSWORD"    # Consider using environment variables for security
receiver_email = "receiver@example.com"

# --- Step 2: Create the email container (MIME multipart) ---
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = "Python Power Shots – Here is your attachment!"

# --- Step 3: Add email body ---
body = "Hello! This email was sent using Python.\nPlease find the attachment below."
message.attach(MIMEText(body, "plain"))

# --- Step 4: Attach a file ---
filename = "sample.pdf"  # Replace with your file

try:
    with open(filename, "rb") as attachment:
        mime_base = MIMEBase("application", "octet-stream")
        mime_base.set_payload(attachment.read())

    # Encode file in base64
    encoders.encode_base64(mime_base)
    mime_base.add_header("Content-Disposition", f"attachment; filename={filename}")

    # Attach to email
    message.attach(mime_base)

except FileNotFoundError:
    print(f"❌ File '{filename}' not found.")
    exit()

# --- Step 5: Connect to SMTP server and send email ---
try:
    # Gmail example (uses TLS)
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()  # Secure the connection
    server.login(sender_email, sender_password)
    server.send_message(message)
    server.quit()

    print("✅ Email sent successfully!")

except Exception as e:
    print("❌ Error sending email:", e)
