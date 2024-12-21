import configparser

class Config:

    def __init__(self, config):
        self.config = config
        self.config.read("config.ini")
        led_1_name = self.config.get("Led_Armed", "name")
        led_1_pin = self.config.getint("Led_Armed", "pin")
        led_2_name = self.config.get("Led_Disarmed", "name")
        led_2_pin = self.config.getint("Led_Disarmed", "pin")
        buzzer_name = self.config.get("Buzzer", "name")
        buzzer_pin = self.config.getint("Buzzer", "pin")
        button_armer_name = self.config.get("Button_Armement", "name")
        button_armer_pin = self.config.getint("Button_Armement", "pin")
        button_armer_conf = self.config.get("Button_Armement", "config")
        button_desarmer_name = self.config.get("Button_Desarmement", "name")
        button_desarmer_pin = self.config.getint("Button_Desarmement", "pin")
        button_desarmer_conf = self.config.get("Button_Desarmement", "config")
        motion_name = self.config.get("Motion_Detection", "name")
        motion_pin = self.config.getint("Motion_Detection", "pin")
        debug_active = self.config.getboolean("General", "debug")

        self.config_data = {
            "led_1_name" : led_1_name,
            "led_1_pin" : led_1_pin,
            "led_2_name" : led_2_name,
            "led_2_pin" : led_2_pin,
            "buzzer_name" : buzzer_name,
            "buzzer_pin" : buzzer_pin,
            "button_armer_name" : button_armer_name,
            "button_armer_pin": button_armer_pin,
            "button_armer_conf": button_armer_conf,
            "button_desarmer_name": button_desarmer_name,
            "button_desarmer_pin": button_desarmer_pin,
            "button_desarmer_conf": button_desarmer_conf,
            "motion_name": motion_name,
            "motion_pin": motion_pin,
            "debug": debug_active
        }
