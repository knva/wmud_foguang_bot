import logging
import time

from event.item import item
from event.room import room
from event.tips import tips
from util import cmd,G_queue

class msg():
    def __init__(self):
        pass

    @staticmethod
    def trigger(message):
        logging.info(message)
        ch = message['ch']

        content = message['content']
        if content == '召唤佛光' and ch =='pty':
            name = message['name']
            uid = message['uid']
            cmd.send('stopstate;dazuo')
            # 添加到全局队列G_queue中
            G_queue.put({'name':name,'ch':ch,'uid':uid,'time':time.time()})
            time.sleep(1)



