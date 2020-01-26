from function import *
from createkey import *
from message import *
from main import *
import time
from db import *


def keyfunc(uid, text, vk, vk_session, event):

    #------------------#
    #Стартовая страница#
    #------------------#

    if text == 'notes':
        notes_key(uid, event, vk)

    elif text == 'timer_notes':
        timenotes_key(uid, event, vk)

    elif text == 'create_notes':
        status = insertcash(uid, 'write')
        if status == 'write':
            vk.messages.send(
                user_id = uid,
                message = 'Введите текст заметки.',
                random_id = get_random_id()
            )
    elif text == 'view_notes':
        titleusernotes = selectusernote(uid)
        status = insertcash(uid, 'selectnumnotes')
        #sendtitlenotes = []
        for i in titleusernotes:
            #sendtitlenotes.append('%s\n'%i)
            vk.messages.send(
                user_id = uid,
                message = i + '\n',
                random_id = get_random_id()
            )
        vk.messages.send(
            user_id = uid,
            message = 'Чтобы просмотреть заметку, нужно написать номер привязанный к ней.',
            random_id = get_random_id()
        )

    elif text == 'test':
        vk.messages.send(
            user_id = uid,
            message = 'Ещё не готово',
            random_id = get_random_id()
        )