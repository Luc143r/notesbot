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
            if status == 'create_notes':
                if (text != '!key') and (text != 'Стандартные заметки') and (text != 'Напоминания') and (text != 'Вызов админа') and (text != 'Напоминания') and (text != 'Создать заметку') and (text != 'Мои заметки') and (text != 'Создать напоминание') and (text != 'Мои напоминания') and (text != 'Назад') and (text != 'Главная') and (text != 'Редактировать заметку') and (text != 'Удалить заметку') and (text != 'Редактировать напоминалку') and (text != 'Удалить напоминалку'):
                    insertnote(uid, text)
                    vk.messages.send(
                        user_id = uid,
                        message = 'Заметка успешно добавлена',
                        random_id = get_random_id()
                    )
            elif status == 'view_notes':
                if (text != '!key') and (text != 'Стандартные заметки') and (text != 'Напоминания') and (text != 'Вызов админа') and (text != 'Напоминания') and (text != 'Создать заметку') and (text != 'Мои заметки') and (text != 'Создать напоминание') and (text != 'Мои напоминания') and (text != 'Назад') and (text != 'Главная') and (text != 'Редактировать заметку') and (text != 'Удалить заметку') and (text != 'Редактировать напоминалку') and (text != 'Удалить напоминалку'):
                    note = selectuserfullnote(int(text), uid)
                    vk.messages.send(
                        user_id = uid,
                        message = note,
                        random_id = get_random_id()
                    )
            elif status == 'edit_note':
                if (text != '!key') and (text != 'Стандартные заметки') and (text != 'Напоминания') and (text != 'Вызов админа') and (text != 'Напоминания') and (text != 'Создать заметку') and (text != 'Мои заметки') and (text != 'Создать напоминание') and (text != 'Мои напоминания') and (text != 'Назад') and (text != 'Главная') and (text != 'Редактировать заметку') and (text != 'Удалить заметку') and (text != 'Редактировать напоминалку') and (text != 'Удалить напоминалку'):
                    result = text.split('.', maxsplit = 1)
                    num = int(result[0])
                    ednote = result[1]
                    editnotes(uid, num, ednote)
                    deletecash(uid)
                    cash = 'view_notes'
                    insertcash(uid, cash)
                    vk.messages.send(
                        user_id = uid,
                        message = 'Заметка успешно отредактирована',
                        random_id = get_random_id()
                    )

            elif status == 'delete_notes':
                if (text != '!key') and (text != 'Стандартные заметки') and (text != 'Напоминания') and (text != 'Вызов админа') and (text != 'Напоминания') and (text != 'Создать заметку') and (text != 'Мои заметки') and (text != 'Создать напоминание') and (text != 'Мои напоминания') and (text != 'Назад') and (text != 'Главная') and (text != 'Редактировать заметку') and (text != 'Удалить заметку') and (text != 'Редактировать напоминалку') and (text != 'Удалить напоминалку'):
                    num = int(text)
                    deletenotes(uid, num)
                    vk.messages.send(
                        user_id = uid,
                        message = 'Заметка успешно удалена',
                        random_id = get_random_id()
                    )
                    deletecash(uid)
                    cash = 'view_notes'
                    insertcash(uid, cash)

            else:
                if (text != '!key') and (text != 'Стандартные заметки') and (text != 'Напоминания') and (text != 'Вызов админа') and (text != 'Напоминания') and (text != 'Создать заметку') and (text != 'Мои заметки') and (text != 'Создать напоминание') and (text != 'Мои напоминания') and (text != 'Назад') and (text != 'Главная') and (text != 'Редактировать заметку') and (text != 'Удалить заметку') and (text != 'Редактировать напоминалку') and (text != 'Удалить напоминалку'):
                    vk.messages.send(
                        user_id = uid,
                        message = 'Выберите пункт меню.',
                        random_id = get_random_id()
                    )
