import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from config import user_token
from config import comm_token
from random import randrange
import requests

vk = vk_api.VkApi(token=comm_token) # Авторизуемся как сообщество
longpoll = VkLongPoll(vk) # Работа с сообщениями


def get_inform(user_id):
    url = f'https://api.vk.com/method/users.get?user_ids={user_id}&fields=bdate,sex,city,relation&access_token={user_token}&v=5.131'
    repl = requests.get(url)
    response = repl.json()
    information_dict = response['response']
    for i in information_dict:
        for key, value in i.items():
            first_name = i.get('first_name')
            last_name = i.get('last_name')
    return first_name

def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': randrange(10 ** 7),})


for event in longpoll.listen():
    print('НАПИШИ')
    if event.type == VkEventType.MESSAGE_NEW: #Если пришло новое сообщение
        if event.to_me: #если оно имеет метку для меня(т.е бота)
            request = event.text  # Сообщение пользователя
            if request == 'Привет' or request == 'привет':
                write_msg(event.user_id, f'Привет, {get_inform("342034365")}')
            elif request == 'Пока':
                write_msg(event.user_id, 'Пока.')
            else:
                write_msg(event.user_id, 'Ваш вопрос непонятен.')


def get_inform_1(self, user_id):
    url = f'https://api.vk.com/method/users.get?user_ids={user_id}&fields=bdate,sex,city,relation&access_token={user_token}&v=5.131'
    repl = requests.get(url)
    response = repl.json()
    information_dict = response['response']
