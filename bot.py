import pywhatkit
import schedule
import time

# Dictionary of contacts and their personalized messages
contacts = {
    "+91 7812874561": "Good morning, MP! Have a fantastic day ahead! ☀️",
    "+91 9080822469": "Rise and shine, Agalya! Wishing you a productive day! 🚀",
    "+91 9345760993": "Hey Anu, Sending you positive vibes for the day! 😊"
}

def send_messages():
    for contact, message in contacts.items():
        pywhatkit.sendwhatmsg_instantly(contact, message)
        print(f"Message sent to {contact}: {message}")

# Schedule the function to run every day at 7:00 AM
schedule.every().day.at("07:00").do(send_messages)

print("WhatsApp Automation Running...")

while True:
    schedule.run_pending()
    time.sleep(60)  # Check every minute
