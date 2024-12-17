from Alarme import Alarme
import RPi.GPIO as GPIO
from State import State

systeme_alarme_1 = Alarme()

try:
    while True:
        match systeme_alarme_1.etat():

            case State.INIT:
                systeme_alarme_1.startup()
                systeme_alarme_1.desarmement(systeme_alarme_1.state)

            case State.DESARMER:
                if systeme_alarme_1.check_input_armer() == 1:
                    systeme_alarme_1.armement()

            case State.ARMER:
                if systeme_alarme_1.check_input_desarmer() == 1:
                    systeme_alarme_1.desarmement(systeme_alarme_1.state)
                if systeme_alarme_1.check_input_motion() == 1:
                    systeme_alarme_1.alarme()

            case State.ALARME:
                if systeme_alarme_1.check_input_desarmer() == 1:
                    systeme_alarme_1.desarmement(systeme_alarme_1.state)
                else:
                    systeme_alarme_1.alarme_led()

except KeyboardInterrupt:
    GPIO.cleanup()