from LED import LED
from Keypad import Keypad
from Buzzer import Buzzer
from Button import Button
from Motion import Motion
from Password import Password
from State import State
from SMTP import SMTP
from Config import Config

import RPi.GPIO as GPIO
import time
import logging
import configparser

class Alarme:
    def __init__(self):
        self.state = State.INIT
        config = configparser.ConfigParser()
        self.config_data = Config(config)
        if self.config_data.config_data["debug"]:
            logging.basicConfig(
                filename='application.log',
                level=logging.DEBUG,
                format='%(asctime)s - %(levelname)s - %(message)s'
            )
        else:
            logging.basicConfig(
                filename='application.log',
                level=logging.INFO,
                format='%(asctime)s - %(levelname)s - %(message)s'
            )

        logging.info("Application en cour d'initialisation.")
    


    def startup(self):
        config_data = self.config_data
        self.rouge = LED(config_data.config_data["led_1_name"], config_data.config_data["led_1_pin"])
        logging.debug("Led " + config_data.config_data["led_1_name"] + " est activer en sortie sur la pin " + str(config_data.config_data["led_1_pin"]))
        self.verte = LED(config_data.config_data["led_2_name"], config_data.config_data["led_2_pin"])
        logging.debug("Led " + config_data.config_data["led_2_name"] + " est activer en sortie sur la pin " + str(config_data.config_data["led_2_pin"]))
        self.buzzer = Buzzer(config_data.config_data["buzzer_name"], config_data.config_data["buzzer_pin"])
        logging.debug("Le " + config_data.config_data["buzzer_name"] + " est activer en sortie sur la pin " + str(config_data.config_data["buzzer_pin"]))

        self.keypad = Keypad(21, 20, 16, 26, 19, 13, 6, 5, "Keypad")
        logging.debug("Keypad Initialiser")
        self.password = Password()
        logging.debug("Objet Password Initialiser")

        self.button_armement = Button(config_data.config_data["button_armer_name"], config_data.config_data["button_armer_pin"], config_data.config_data["button_armer_conf"])
        logging.debug("Button " + config_data.config_data["button_armer_name"] + " est configurer en pull-" + config_data.config_data["button_armer_conf"] + " sur la pin " + str(config_data.config_data["button_armer_pin"]))
        self.button_desarmement = Button(config_data.config_data["button_desarmer_name"], config_data.config_data["button_desarmer_pin"], config_data.config_data["button_desarmer_conf"])
        logging.debug("Button " + config_data.config_data["button_desarmer_name"] + " est configurer en pull-" + config_data.config_data["button_desarmer_conf"] + " sur la pin " + str(config_data.config_data["button_desarmer_pin"]))
        self.motion = Motion(config_data.config_data["motion_name"], config_data.config_data["motion_pin"])
        logging.debug("Le " + config_data.config_data["motion_name"] + " est configurer en entrer sur la pin " + str(config_data.config_data["motion_pin"]))
        logging.info("Initialisation des composanted completer")

    def desarmement(self, state):
        if  state == State.INIT or self.password.input_password(self.keypad, self.buzzer):
            logging.info("En cour de desarmement")
            self.verte.led_on()
            logging.debug(self.verte)
            self.rouge.led_off()
            logging.debug(self.rouge)
            self.buzzer.buzzer_off()
            logging.debug(self.buzzer)

            self.state = State.DESARMER
            logging.info("Systeme desarmer")

    def armement(self):
        if self.password.input_password(self.keypad, self.buzzer):
            logging.info("En cour de Armement")
            self.verte.led_off()
            logging.debug(self.verte)
            self.rouge.led_on()
            logging.debug(self.rouge)
            self.buzzer.buzzer_off()
            logging.debug(self.buzzer)

            logging.info("Delai d'armement en cour")
            time.sleep(5)
            logging.info("Delai completer.")

            self.state = State.ARMER
            logging.info("Systeme Armer")

    def alarme(self):
        logging.info("Mouvement detecter")
        self.buzzer.buzzer_on()
        logging.debug(self.buzzer)
        logging.info("Initialisation de l'envois de courriel")
        self.alarme_email()
        logging.info("Finalisation de l'envois de courriel.")
        self.state = State.ALARME
        logging.info("En alarme!")

    def alarme_led(self):
        self.rouge.led_flash()

    def alarme_email(self):
        logging.debug("Initialisation de l'objet SMTP")
        try:
            self.email = SMTP()
        except:
            logging.warning("Impossible de completer la connection avec le serveur smtp, 0x01")
            return
        logging.debug("Initialisation completer.")
        logging.debug("Envoie de la commende ehlo au server")
        try:
            self.email.identify()
        except:
            logging.warning("Impossible de completer la connection avec le serveur smtp. 0x02")
            return
        logging.debug("Initialisation du TLS")
        self.email.secure()
        logging.debug("TLS completer")
        logging.debug("Logging au serveur")
        try:
            self.email.login()
        except:
            logging.warning("Impossible de completer la connection avec le serveur smtp. 0x03")
            return
        logging.debug("Login completer avec succes")
        logging.debug("envoie du courriel")
        self.email.send_email()
        logging.debug("Courriel envoyer")
        self.email.end_session
        del self.email
        logging.debug("Fin de la session SMTP")

    def check_input_armer(self):
        if self.button_armement.detection():
            return 1
        else:
            return 0

    def check_input_desarmer(self):
        if not self.button_desarmement.detection():
            return 1
        else:
            return 0

    def check_input_motion(self):
        if self.motion.detection():
            return 1
        else:
            return 0

    def etat(self):
        return self.state

    def __str__(self):
        print("Etat actuel du systeme")
        print(self.state)
        print(self.verte)
        print(self.rouge)
        print(self.buzzer)
        return "Done"
