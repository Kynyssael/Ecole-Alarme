#Classe Buzzer, Permet de configuer les Buzzer et de les alumer et eteindre.
import RPi.GPIO as GPIO
import time

class Buzzer:
    def __init__(self, name, pin):
        GPIO.setmode(GPIO.BCM)
        self.name = name
        self.pin = pin
        self.state = "Off"
        GPIO.setup(self.pin, GPIO.OUT)
        GPIO.output(self.pin, GPIO.LOW)

    def buzzer_on(self):
        GPIO.output(self.pin, GPIO.HIGH)
        self.state = "On"

    def buzzer_off(self):
        GPIO.output(self.pin, GPIO.LOW)
        self.state = "Off"

    def buzzer_input(self):
        self.buzzer_on()
        time.sleep(0.1)
        self.buzzer_off()
        time.sleep(0.1)

    def __str__(self):
        return "Etat du buzzer " + self.name + ": " + self.state