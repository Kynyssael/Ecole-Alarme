import smtplib
import datetime;

class SMTP:

    def __init__(self):
        print("INIT")
        self.smtpObj = smtplib.SMTP("smtp.gmail.com", 587)
        print("INIT DONE")

    def identify(self):
        self.smtpObj.ehlo()
    
    def secure(self):
        print("Secure")
        self.smtpObj.starttls()

    def login(self):
        print("Login")
        self.smtpObj.login("drecz30@gmail.com", "fzgt hksh irkx fcdd")

    def send_email(self):
        from_address = "drecz30@gmail.com"
        to_address = "drecz30@gmail.com"
        message = f"""\
        Subject: Alerte detecte
        To:{to_address}
        From:{from_address}

        Alerte Detecter. Verifier le systeme. Timestamp : {datetime.datetime.now()}"""

        self.smtpObj.sendmail(from_address, to_address, message)

    def end_session(self):
        self.smtpObj.quit()