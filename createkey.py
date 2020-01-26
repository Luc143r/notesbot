from message import *
from function import *
from main import *
from funckey import *
from vk_api.keyboard import VkKeyboard, VkKeyboardColor

#------------------#
#Стартовая страница#
#------------------#

def start_keyboard(uid, event, vk):

        keyboard = VkKeyboard(one_time=False)

        keyboard.add_button(
            'Стандартные заметки',
            color=VkKeyboardColor.POSITIVE,
            payload = {'key': 'notes'}
        )
        keyboard.add_button(
            'Напоминания',
            color = VkKeyboardColor.NEGATIVE,
            payload = {'key': 'timer_notes'}
        )

        keyboard.add_line()

        keyboard.add_vkpay_button(hash = 'action=transfer-to-user&user_id=127949564', payload={'key': 'donate'})

        vk.messages.send(
            user_id = uid,
            message = 'Управляйте ботом с помощью кнопок',
            keyboard = keyboard.get_keyboard(),
            random_id = get_random_id())

def notes_key(uid, event, vk):
    keyboard = VkKeyboard(one_time=False)

    keyboard.add_button(
        'Создать заметку',
        color=VkKeyboardColor.POSITIVE,
        payload = {'key': 'create_notes'}
    )
    keyboard.add_button(
        'Мои заметки',
        color = VkKeyboardColor.NEGATIVE,
        payload = {'key': 'view_notes'}
    )
    vk.messages.send(
        user_id = uid,
        message = 'Управляйте ботом с помощью кнопок',
        keyboard = keyboard.get_keyboard(),
        random_id = get_random_id())

def timenotes_key(uid, event, vk):
    keyboard = VkKeyboard(one_time=False)

    keyboard.add_button(
        'Создать напоминание',
        color=VkKeyboardColor.POSITIVE,
        payload = {'key': 'create_timenotes'}
    )
    keyboard.add_button(
        'Мои напоминания',
        color = VkKeyboardColor.NEGATIVE,
        payload = {'key': 'view_timenotes'}
    )
    vk.messages.send(
        user_id = uid,
        message = 'Управляйте ботом с помощью кнопок',
        keyboard = keyboard.get_keyboard(),
        random_id = get_random_id())