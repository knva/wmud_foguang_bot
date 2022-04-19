import logging
from util import cmd


class item():
    items = ''
    def __init__(self):
        pass
    @staticmethod
    def trigger(message):
        logging.info("items.trigger")
        print(message)
        item.items= message['items']


