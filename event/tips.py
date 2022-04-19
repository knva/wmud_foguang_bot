import logging
from util import cmd, Role


class tips():
    msgs = []
    def __init__(self):
        pass
    @staticmethod
    def trigger(message):
        logging.info("tips.trigger")
        print(message)
        if len(tips.msgs)==100:
            tips.msgs =[]
        tips.msgs.append(message['text'])
        if '{}重新连线'.format(Role['name']) in message['text']:
            cmd.send('stopstate;team out;dazuo')
    @staticmethod
    def info(message):
        logging.info("tips.info")
        print(message)
        while True:
            for i in tips.msgs:
                if message in i:
                    tips.msgs= []
                    return True
