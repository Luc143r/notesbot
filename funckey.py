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
        deletecash(uid)
        cash = 'notes'
        insertcash(uid, cash)
        notes_key(uid, event, vk)

    elif text == 'create_notes':
        deletecash(uid)
        cash = 'create_notes'
        status = insertcash(uid, cash)
        if status == 'create_notes':
            vk.messages.send(
                user_id = uid,
                message = 'Введите текст заметки.',
                random_id = get_random_id()
            )

    elif text == 'home':
        start_keyboard(uid, event, vk)
    
    elif text == 'back':
        status = checkcash(uid)
        if status == 'view_notes':
            notes_key(uid, event, vk)
            deletecash(uid)

    elif text == 'view_notes':
        deletecash(uid)
        cash = 'view_notes'
        titleusernotes = selectusernote(uid)
        status = insertcash(uid, cash)
        #sendtitlenotes = []
        for i in titleusernotes:
            #sendtitlenotes.append('%s\n'%i)
            vk.messages.send(
                user_id = uid,
                message = i + '\n',
                random_id = get_random_id()
            )
        view_notes_key(uid, event, vk)

    elif text == 'edit_note':
        deletecash(uid)
        cash = 'edit_note'
        vk.messages.send(
            user_id = uid,
            message = 'Введите номер и текст новой заметки в формате: <id>.<text>\nПример: \n1.Это новый текст, который будет в этой заметке!',
            random_id = get_random_id()
        )
        status = insertcash(uid, cash)

    elif text == 'delete_notes':
        deletecash(uid)
        cash = 'delete_notes'
        vk.messages.send(
            user_id = uid,
            message = 'Введите номер заметки, которую необходимо удалить',
            random_id = get_random_id()
        )
        status = insertcash(uid, cash)


