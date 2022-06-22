from keyboard import keyboard, sender
from vk_api.longpoll import VkLongPoll, VkEventType
from config import user_token, comm_token, offset
from main import *

def send_photo_1(user_id, message):
    vk.method("messages.send", {"user_id": user_id,
                                'access_token': user_token,
                                'message': message,
                                'attachment': f'photo{person_id(offset)}_{get_photo_1(person_id(offset))}',
                                "random_id": 0})

def send_photo_2(user_id, message):
    vk.method("messages.send", {"user_id": user_id,
                                'access_token': user_token,
                                'message': message,
                                'attachment': f'photo{person_id(offset)}_{get_photo_2(person_id(offset))}',
                                "random_id": 0})

def send_photo_3(user_id, message):
    vk.method("messages.send", {"user_id": user_id,
                                'access_token': user_token,
                                'message': message,
                                'attachment': f'photo{person_id(offset)}_{get_photo_3(person_id(offset))}',
                                "random_id": 0})

def find_persons(user_id, offset):
    write_msg(user_id, found_person_info(offset))
    person_id(offset)
    insert_data_seen_users(person_id(offset), offset )
    get_photos_id(person_id(offset))
    send_photo_1(user_id, 'Фото номер 1')
    if get_photo_2(person_id(offset)) != None:
        send_photo_2(user_id, 'Фото номер 2')
        send_photo_3(user_id, 'Фото номер 3')
    else:
        write_msg(user_id, f'Больше фотографий нет')

line = range(0,100)
#drop_seen_users()
#create_table_seen_users()

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        request = event.text.lower()
        user_id = str(event.user_id)
        msg = event.text.lower()
        sender(user_id, msg.lower())
        if request == 'начать поиск':
            write_msg(event.user_id, f'Здравствуй, {name(user_id)}') # , твой id - {user_id}
            find_user(user_id)
            find_persons(user_id, offset)

        elif request == 'вперёд':
            for i in line:
                #if request == 'вперёд':
                offset += 1
                find_persons(user_id, offset)
                break
        else:
            write_msg(event.user_id, 'Ваш вопрос непонятен.')
