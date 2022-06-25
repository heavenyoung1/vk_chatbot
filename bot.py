from keyboard import keyboard, sender
from vk_api.longpoll import VkLongPoll, VkEventType
from config import user_token, comm_token, offset, line
from main import *


for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        request = event.text.lower()
        user_id = str(event.user_id)
        msg = event.text.lower()
        sender(user_id, msg.lower())
        if request == 'начать поиск':
            creating_database()
            write_msg(event.user_id, f'Привет, {name(user_id)}')
            find_user(user_id)
            write_msg(event.user_id, f'Нашёл для тебя пару, жми на кнопку "Вперёд"')
            find_persons(user_id, offset)

        elif request == 'вперёд':
            for i in line:
                offset += 1
                find_persons(user_id, offset)
                break
        elif request == 'назад':
            write_msg(user_id, 'Жми вперёд')

        else:
            write_msg(event.user_id, 'Твоё сообщение непонятно')
