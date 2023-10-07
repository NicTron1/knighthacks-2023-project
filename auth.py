import smtplib
from email.message import EmailMessage

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login("troncosolnicolas@gmail.com", "vcivkqydcufkjbmm")

msg = EmailMessage()
msg["Subject"] = "Test"
msg["From"] = "Project <troncosolnicolas@gmail.com>"
msg["To"] = "Nicolas Troncoso <nicolasltroncoso@gmail.com>"
msg.set_content("Test email.")

server.send_message(msg)
server.quit()