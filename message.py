from function import *
from message import *
#from main import *
from createkey import *
from funckey import *
from db import *

def messages(event, vk_session, vk, longpoll, upload, uid, text, start_keyboard):
    if event.obj.peer_id < 2000000000:
        if uid > 0:
            if text == '!key':
                start_keyboard(uid, event, vk)
            status = checkcash(uid)
            if status == 'write':
                if (text != '!key') and (text != 'Стандартные заметки') and (text != 'Напоминания') and (text != 'Вызов админа') and (text != 'Напоминания') and (text != 'Создать заметку') and (text != 'Мои заметки') and (text != 'Создать напоминание') and (text != 'Мои напоминания'):
                    insertnote(uid, text)
                    vk.messages.send(
                        user_id = uid,
                        message = 'Заметка успешно добавлена',
                        random_id = get_random_id()
                    )
            elif status == 'selectnumnotes':
                if (text != '!key') and (text != 'Стандартные заметки') and (text != 'Напоминания') and (text != 'Вызов админа') and (text != 'Напоминания') and (text != 'Создать заметку') and (text != 'Мои заметки') and (text != 'Создать напоминание') and (text != 'Мои напоминания'):
                    note = selectuserfullnote(int(text), uid)
                    vk.messages.send(
                        user_id = uid,
                        message = note,
                        random_id = get_random_id()
                    )

            else:
                if (text != 'Стандартные заметки') and (text != 'Напоминания') and (text != 'Вызов админа') and (text != 'Напоминания') and (text != 'Создать заметку') and (text != 'Мои заметки') and (text != 'Создать напоминание') and (text != 'Мои напоминания'):
                    vk.messages.send(
                        user_id = uid,
                        message = 'Выберите пункт меню.',
                        random_id = get_random_id()
                    )
