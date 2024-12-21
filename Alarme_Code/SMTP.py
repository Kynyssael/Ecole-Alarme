import smtplib
import datetime
from dotenv import load_dotenv
import os

class SMTP:

    def __init__(self):
        self.smtpObj = smtplib.SMTP("smtp.gmail.com", 587)
        load_dotenv()
        print(os.getenv("SMTP_DEFAULT_EMAIL"))

    def identify(self):
        self.smtpObj.ehlo()
    
    def secure(self):
        self.smtpObj.starttls()

    def login(self):
        self.smtpObj.login(os.getenv("SMTP_DEFAULT_EMAIL"), os.getenv("SMTP_DEFAULT_PASS"))

    def send_email(self):
        from_address = os.getenv("SMTP_DEFAULT_EMAIL")
        to_address = os.getenv("SMTP_DEFAULT_EMAIL")
        message = f"""\
        Subject: Alerte detecte
        To:{to_address}
        From:{from_address}

        Alerte Detecter. Verifier le systeme. Timestamp : {datetime.datetime.now()}"""

        self.smtpObj.sendmail(from_address, to_address, message)

    def end_session(self):
        self.smtpObj.quit()