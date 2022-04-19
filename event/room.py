import logging
from util import cmd,Role


class room():
    name = ''
    def __init__(self):
        room.name = ''
    @staticmethod
    def trigger(message):
        logging.info("room.trigger")
        print(message)
        room.name= message['name']
        Role['room'] = message['name']
        print('room.name',room.name)

