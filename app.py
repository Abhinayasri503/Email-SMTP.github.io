import smtplib
import os
from dotenv import load_dotenv
load_dotenv()
EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_PORT = int(os.getenv("EMAIL_PORT"))
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
recipients=[
    "duttalurusindhujareddy@gmail.com",
    "haarshithamaigadela@gmail.com"
]
message = """Subject:Python Training Notification

Hello,

This is a your Friend  abhinaya

Please reply to this email.

Regards,
Abhinaya Sri
alamuruabhinayasri@gmail.com
8142606517
"""
server = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
server.starttls()
server.login(EMAIL_USER, EMAIL_PASSWORD)
for receiver in recipients:
    server.sendmail(
        EMAIL_USER,
        receiver,
        message
    )
    print(f"Email sent succesfully to {receiver}")
server.quit()