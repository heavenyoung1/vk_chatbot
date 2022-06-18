import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from config import user_token
from config import comm_token
from random import randrange
import requests
from main import *
from vk_api.keyboard import VkKeyboard, VkKeyboardColor

vk = vk_api.VkApi(token=comm_token) # Авторизуемся как сообщество
longpoll = VkLongPoll(vk) # Работа с сообщениями

def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id,
                                'message': message,
                                'random_id': randrange(10 ** 7)
                                })
def send_photo(user_id, message):
    vk.method("messages.send", {"user_id": user_id,
                                'access_token': user_token,
                                'message': f'photo{user_id}_{get_photo_1(user_id)}',
                                'attachment': f'photo{user_id}_{get_photo_1(user_id)}',
                                "random_id": 0})

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        request = event.text.lower()
        user_id = str(event.user_id)
        find_city(user_id)
        get_photos_id(event.user_id)
        if request == 'привет':
            write_msg(event.user_id, f'Привет, {name(user_id)}') # , твой id - {user_id}
            write_msg(event.user_id, get_sex(user_id))
            write_msg(event.user_id, city_id(user_id))
            get_age(event.user_id)
            #write_msg(event.user_id, get_age(user_id))
            #send_photo(user_id, 'mmm')
            #write_msg(event.user_id, find_user(user_id))

        elif request == 'Пока':
            write_msg(event.user_id, 'Пока.')
        else:
            write_msg(event.user_id, 'Ваш вопрос непонятен.')


    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            request = event.text
