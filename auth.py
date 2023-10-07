import smtplib
import random
from email.message import EmailMessage

def sendOTP(destination, otp):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("troncosolnicolas@gmail.com", "vcivkqydcufkjbmm")

    msg = EmailMessage()
    msg["Subject"] = "Test"
    msg["From"] = "Authentication <troncosolnicolas@gmail.com>"
    msg["To"] = destination
    msg.set_content("Here is your one-time login code: " + otp)

    server.send_message(msg)
    server.quit()

def genOTP():
    return random.randint(10000, 99999)
