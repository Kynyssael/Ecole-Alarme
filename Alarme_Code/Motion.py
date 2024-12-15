import RPi.GPIO as GPIO

class Motion:
    def __init__(self, name, pin):
        GPIO.setmode(GPIO.BCM)
        self.name = name
        self.pin = pin
        GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    def detection(self):
        return GPIO.input(self.pin)