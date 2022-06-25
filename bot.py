from keyboard import sender
from main import *


for event in bot.longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        request = event.text.lower()
        user_id = str(event.user_id)
        msg = event.text.lower()
        sender(user_id, msg.lower())
        if request == 'начать поиск':
            creating_database()
            bot.write_msg(user_id, f'Привет, {bot.name(user_id)}')
            bot.find_user(user_id)
            bot.write_msg(event.user_id, f'Нашёл для тебя пару, жми на кнопку "Вперёд"')
            bot.find_persons(user_id, offset)

        elif request == 'вперёд':
            for i in line:
                offset += 1
                bot.find_persons(user_id, offset)
                break

        else:
            bot.write_msg(event.user_id, 'Твоё сообщение непонятно')
