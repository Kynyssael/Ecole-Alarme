#Classe Button, Permet de configuer les Bouton
import RPi.GPIO as GPIO

class Button:
    def __init__(self, name, pin, config):
        GPIO.setmode(GPIO.BCM)
        self.name = name
        self.pin = pin
        if config == "down":
            GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        if config == "up":
            GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def detection(self):
        return GPIO.input(self.pin)