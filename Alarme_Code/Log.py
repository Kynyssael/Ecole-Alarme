import logging

class Log:
    def __init__(self, bool):
        if bool:
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