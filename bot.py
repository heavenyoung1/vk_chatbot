import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from config import user_token
from config import comm_token
from random import randrange
import requests
from main import *
vk = vk_api.VkApi(token=comm_token) # Авторизуемся как сообщество
longpoll = VkLongPoll(vk) # Работа с сообщениями

def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id,
                                'message': message,
                                'random_id': randrange(10 ** 7)
                                })

def photo_sender(user_id):
    vk.method('message.send', {'user_id': user_id,
                               'attachment' : 'photo' + str(get_photo(user_id)),
                               'random_id': randrange(10 ** 7)})

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW: #Если пришло новое сообщение
        if event.to_me: #если оно имеет метку для меня(т.е бота)
            request = event.text  # Сообщение пользователя
            user_id = str(event.user_id)
            find_city(user_id)
            #find_user(user_id)
            if request == 'Привет' or request == 'привет':
                write_msg(event.user_id, f'Привет, {name(user_id)}, твой id - {user_id}')
                #write_msg(event.user_id, get_sex(user_id))
                #age_to()
                #age_from()
                send_photo(event.user_id, get_photo(user_id))
                write_msg(event.user_id, get_photo(user_id))
                write_msg(event.user_id, city_id(user_id))
                #write_msg(event.user_id, get_age(user_id))
                write_msg(event.user_id, find_user(user_id))

            elif request == 'Пока':
                write_msg(event.user_id, 'Пока.')
            else:
                write_msg(event.user_id, 'Ваш вопрос непонятен.')

    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            request = event.text


