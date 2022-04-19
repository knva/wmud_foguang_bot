import logging


class dialog():

    def __init__(self):
        pass
        
    @staticmethod
    def trigger(message):
        logging.info("Triggering dialog")
        print(message)