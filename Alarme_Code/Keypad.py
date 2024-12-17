#Class Keypad pour configurer et lire le keypad
import RPi.GPIO as GPIO
import time

class Keypad:

    def __init__(self, l1, l2, l3, l4, c1, c2, c3, c4, name):
        self.last_input = None
        self.l1 = l1
        self.l2 = l2
        self.l3 = l3
        self.l4 = l4
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3
        self.c4 = c4
        self.name = str(name)


        GPIO.setmode(GPIO.BCM)

        GPIO.setup(self.l1, GPIO.OUT)
        GPIO.setup(self.l2, GPIO.OUT)
        GPIO.setup(self.l3, GPIO.OUT)
        GPIO.setup(self.l4, GPIO.OUT)

        self.__all_line_high()

        GPIO.setup(self.c1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.c2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.c3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.c4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

        self.__activate_event_detection()

    def reset_pin(self):
        self.last_input = None

    def __activate_event_detection(self):
        GPIO.add_event_detect(self.c1, GPIO.RISING, callback=self.__read_keypad, bouncetime=200)
        GPIO.add_event_detect(self.c2, GPIO.RISING, callback=self.__read_keypad, bouncetime=200)
        GPIO.add_event_detect(self.c3, GPIO.RISING, callback=self.__read_keypad, bouncetime=200)
        GPIO.add_event_detect(self.c4, GPIO.RISING, callback=self.__read_keypad, bouncetime=200)

    def __remove_event_detection(self):
        GPIO.remove_event_detect(self.c1)
        GPIO.remove_event_detect(self.c2)
        GPIO.remove_event_detect(self.c3)
        GPIO.remove_event_detect(self.c4)

    def __all_line_high(self):
        GPIO.output(self.l1, GPIO.HIGH)
        GPIO.output(self.l2, GPIO.HIGH)
        GPIO.output(self.l3, GPIO.HIGH)
        GPIO.output(self.l4, GPIO.HIGH)

    def __all_line_low(self):
        GPIO.output(self.l1, GPIO.LOW)
        GPIO.output(self.l2, GPIO.LOW)
        GPIO.output(self.l3, GPIO.LOW)
        GPIO.output(self.l4, GPIO.LOW)

    def __read_input_keypad(self, characters, line):
        GPIO.output(line, GPIO.HIGH)
        if(GPIO.input(self.c1) == 1):
            GPIO.output(line, GPIO.LOW)
            return characters[0]
        if(GPIO.input(self.c2) == 1):
            GPIO.output(line, GPIO.LOW)
            return characters[1]
        if(GPIO.input(self.c3) == 1):
            GPIO.output(line, GPIO.LOW)
            return characters[2]
        if(GPIO.input(self.c4) == 1):
            GPIO.output(line, GPIO.LOW)
            return characters[3]
        GPIO.output(line, GPIO.LOW)
        return None

    def __read_keypad(self, channel):

        self.__remove_event_detection()

        self.__all_line_low()

        char = self.__read_input_keypad(["1","2","3","A"], self.l1)
        if char != None:
            self.last_input = char
            self.__all_line_high()
            self.__activate_event_detection()
            return
        char = self.__read_input_keypad(["4","5","6","B"], self.l2)
        if char != None:
            self.last_input = char
            self.__all_line_high()
            self.__activate_event_detection()
            return
        char = self.__read_input_keypad(["7","8","9","C"], self.l3)
        if char != None:
            self.last_input = char   
            self.__all_line_high()
            self.__activate_event_detection()
            return       
        char = self.__read_input_keypad(["*","0","#","D"], self.l4)
        if char != None:
            self.last_input = char
            self.__all_line_high()
            self.__activate_event_detection()
            return
        self.__all_line_high()
        self.__activate_event_detection()
        return

