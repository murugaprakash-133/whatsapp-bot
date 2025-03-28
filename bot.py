import pywhatkit
import schedule
import time
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Dictionary of contacts and their personalized messages
contacts = {
    os.getenv("MP_NUMBER"): "Good morning, MP! Have a fantastic day ahead! ☀️",
    os.getenv("AGALYA_NUMBER"): "Rise and shine, Agalya! Wishing you a productive day! 🚀",
    os.getenv("ANU_NUMBER"): "Hey Anu, Sending you positive vibes for the day! 😊"
}

def send_messages():
    for contact, message in contacts.items():
        if contact:  # Ensure the contact is not None
            pywhatkit.sendwhatmsg_instantly(contact, message)
            print(f"Message sent to {contact}: {message}")

# Schedule the function to run every day at 7:00 AM
schedule.every().day.at("07:00").do(send_messages)

print("WhatsApp Automation Running...")

while True:
    schedule.run_pending()
    time.sleep(60)  # Check every minute
