from LED import LED
from Keypad import Keypad
from Buzzer import Buzzer
from Button import Button
from Motion import Motion
from Password import Password
from State import State

import RPi.GPIO as GPIO
import time

class Alarme:
    def __init__(self):
        self.state = State.INIT

    def startup(self):
        self.rouge = LED("rouge", 18)
        self.verte = LED("verte", 25)
        self.buzzer = Buzzer("buzzer_main", 24)
        self.keypad = Keypad(21, 20, 16, 26, 19, 13, 6, 5, "Keypad")
        self.password = Password()

        self.button_armement = Button("armement", 17, "down")
        self.button_desarmement = Button("desarmement", 27, "up")
        self.motion = Motion("Motion_1", 22)

    def desarmement(self, state):
        if  state == State.INIT or self.password.input_password(self.keypad, self.buzzer):
            self.verte.led_on()
            self.rouge.led_off()
            self.buzzer.buzzer_off()

            self.state = State.DESARMER

    def armement(self):
        if self.password.input_password(self.keypad, self.buzzer):
            self.verte.led_off()
            self.rouge.led_on()
            self.buzzer.buzzer_off()

            time.sleep(5)

            self.state = State.ARMER

    def alarme(self):
        self.buzzer.buzzer_on()
        self.state = State.ALARME

    def alarme_led(self):
        self.rouge.led_flash()

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
