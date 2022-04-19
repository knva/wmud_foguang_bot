import logging

from util import cmd, Role


class roles():
    def __init__(self):
        pass
    @staticmethod
    def trigger( message):
        logging.info("roles.trigger")
        idx = 1
        for item in message['roles']:
            print('{}:{}'.format(idx,item['name']))
            idx=idx+1

        flag = True
        if Role['uid']!="":
            cmd.send('login {}'.format(Role['uid']))
            flag = False
        while flag:
            try:
                selectrole = int(input("Select role: "))
                logging.info('选择角色: ' + message['roles'][selectrole-1]['name'])
                cmd.send('login {}'.format(message['roles'][selectrole-1]['id']))
                Role['uid'] = message['roles'][selectrole-1]['id']
                Role['name']=message['roles'][selectrole-1]['name']
                flag = False
            except Exception as e:
                logging.warning('登录异常,请重试')

