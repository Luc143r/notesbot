import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api import VkUpload
from vk_api.utils import get_random_id
import requests
from threading import *
import os
from random import *
from funckey import *
from createkey import *
from message import *
from function import *

#Group: https://vk.com/stupiddevelopergroup

def main():
    vk_session = vk_api.VkApi(token = 'd9ec11dce7ebaa63b6ce9fcc01ffab7a11e7bcedd7e5797c2464f82959b947a4a724fb4097fb46a764c69')
    print('Bot started!')

    vk = vk_session.get_api()
    group_id = 179311430

    longpoll = VkBotLongPoll(vk_session, str(group_id))
    upload = vk_api.VkUpload(vk_session)

    def listener(event, vk, vk_session, upload, longpoll, group_id):
        if event.type == VkBotEventType.MESSAGE_NEW and event.object.text.strip()!='':
            uid = event.obj.from_id
            text = event.obj.text
            messages(event, vk_session, vk, longpoll, upload, uid, text, start_keyboard)
        if 'payload' in event.object:
            payload = event.object['payload']
            if payload[:8] == '{"key":"':
                uid = event.obj.from_id
                text = payload[8:][:-2]
                keyfunc(uid, text, vk, vk_session, event)

    for event in longpoll.listen():
        listen = Thread( target = listener, name = str(random()), args = (event, vk, vk_session, upload, longpoll, group_id) )
        listen.start()

if __name__ == "__main__":
    main()