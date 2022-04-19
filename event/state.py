import logging
import time

from event import room, tips
from util import cmd, G_queue, Role


class state():
    state = ''
    skills = []
    def __init__(self):
        pass
    @staticmethod
    def trigger(message):
        logging.info("state.trigger")
        # print(message)
        if 'state' in message:

            state.state= message['state']
            print(state.state)
            if '挖矿中' in state.state or '闭关' in state.state:  # 什么 竟然还有武帝
                # 查找G_queue队列中是否存在任务
                taskdata = G_queue.get()
                uid = taskdata['uid']
                name = taskdata['name']
                ch = taskdata['ch']
                cmd.send('stopstate;jh fam 0 start;go north;go north;enable force yijinjing2')

                time.sleep(2)
                if Role['room'] == '扬州城-北大街':

                    cmd.send("{} 请『{}』到武庙门口等候加持佛光".format(ch, name))
                    dofoguang = True
                    idx = 0
                    while dofoguang:
                        cmd.send('team out;team add {}'.format(uid))
                        if tips.info("{}加入队伍".format(name)):
                            time.sleep(1)
                            cmd.send('perform force.foguang')
                            cmd.send('team out')
                            time.sleep(25)  # 等待技能cd
                            cmd.send('dazuo')
                            dofoguang = False
                        time.sleep(1)
                        idx = idx +1
                        # 如果计数器达到60 则退出循环
                        if idx ==60:
                            dofoguang = False
                            cmd.send('team out;dazuo')
        else:
            state.state=''

