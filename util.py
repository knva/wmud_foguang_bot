import time
import queue
G_WS= None
G_queue = queue.Queue()
Role = {'state':'', 'uid':'','name':'','level':'','room':''}
class cmd():
    def __init__(self):
        pass

    @staticmethod
    def send(cmd):
        if G_WS!=None:
            cmd = cmd.split(";")
            for i in cmd:
                time.sleep(0.3)
                print('send:',i)
                G_WS.send(i)