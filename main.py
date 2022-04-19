import threading

import websocket
import _thread
import time
import rel

import util
from event import *

from wsgamelogin import GetLoginInfo

G_COOKIE= ''
G_ROLE_ID = ''


def convet_json(json_str):
    if "{" and "}" in json_str:
        json_obj = eval(json_str, type('Dummy', (dict,), dict(__getitem__=lambda s, n: n))())

    else:
        json_obj = {"type": "tips", "text": json_str}

    return json_obj


def on_message(ws, message):
    def run(*args):
        res_data = convet_json(message)
        if res_data['type'] =='roles':
            roles.trigger(res_data)
        elif res_data['type']== 'tips':
            tips.trigger(res_data)
        elif res_data['type'] == 'dialog':
            dialog.trigger(res_data)
        elif res_data['type']=='room':
            room.trigger(res_data)
        elif res_data['type']=='state':
            state.trigger(res_data)
        elif res_data['type'] == 'msg':
            msg.trigger(res_data)

        # print(res_data)
    threading.Thread(target=run, args=()).start()




def on_error(ws, error):
    print(error)
    print("### error ###")

def on_close(ws, close_status_code, close_msg):
    print("### closed ###")

def on_open(ws):
    print("Opened connection")
    util.G_WS = ws
    ws.send(G_COOKIE)


if __name__ == "__main__":
    # login to sever
    # input username and password and area
    username = input("Username: ")
    password = input("Password: ")
    area = input("Area: ")
    # connect to server
    userdata = GetLoginInfo(username, password)
    G_COOKIE = userdata.getCookie()
    serverurl = userdata.getServerUrl(area)

    # websocket.enableTrace(True)
    keep_on =True
    while keep_on:
        try:
            ws = websocket.WebSocketApp(serverurl,
                                      on_open=on_open,
                                      on_message=on_message,
                                      on_error=on_error,
                                      on_close=on_close)

            ws.run_forever()
        except:
            pass
