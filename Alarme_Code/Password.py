import inputimeout
from Keypad import Keypad
from Buzzer import Buzzer

import RPi.GPIO as GPIO
import time

class Password:

    def __init__(self):
        self.password = "1234"

    def input_password(self, keypad, buzzer):
        last_buzzer_state = buzzer.state
        buzzer.buzzer_off()
        enteredPassword = ""
        timeoutSecond = 20
        start_time = time.time()
        keypad.reset_pin()
        last_key_press = keypad.last_input

        while time.time() - start_time < timeoutSecond:
            last_key_press = keypad.last_input
            if last_key_press is not None:
                if last_key_press == "#":
                    buzzer.buzzer_input()
                    break
                elif last_key_press == "*":
                    buzzer.buzzer_input()
                    keypad.reset_pin()
                    last_key_press = keypad.last_input
                    enteredPassword = ""
                else:
                    enteredPassword = enteredPassword+str(last_key_press)
                    buzzer.buzzer_input()
                    keypad.reset_pin()
                    last_key_press = keypad.last_input
                    print(enteredPassword)
            
        if enteredPassword == self.password:
            buzzer.buzzer_input()
            buzzer.buzzer_input()
            print(enteredPassword)
            return True
        else:
            print(enteredPassword)
            buzzer.buzzer_input()
            buzzer.buzzer_input()
            buzzer.buzzer_input()
            if last_buzzer_state == "Off":
                buzzer.buzzer_off()
            else:
                buzzer.buzzer_on()
            return False