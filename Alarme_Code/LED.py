#Classe LED, Permet de configuer les LED et de les alumer et eteindre.
import RPi.GPIO as GPIO
import time
import logging

class LED:
    def __init__(self, name, pin):
        GPIO.setmode(GPIO.BCM)
        self.name = str(name)
        self.pin = pin
        self.state = "Off"
        GPIO.setup(self.pin, GPIO.OUT)
        GPIO.output(self.pin, GPIO.LOW)

    def led_on(self):
        GPIO.output(self.pin, GPIO.HIGH)
        self.state = "On"

    def led_off(self):
        GPIO.output(self.pin, GPIO.LOW)
        self.state = "Off"

    def led_flash(self):
        if self.state == "On":
            self.led_off()
        else:
            self.led_on()
        time.sleep(0.15)

    def __str__(self):
        return "Etat de la LED " + self.name + ": " + self.state