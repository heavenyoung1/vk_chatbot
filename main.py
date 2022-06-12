import vk_api
import requests
import datetime
from vk_api.longpoll import VkLongPoll, VkEventType
from config import user_token
from config import comm_token
from random import randrange
import json
from pprint import pprint


class VKBot():
    def __init__(self, user_id):
        self.user_id = user_id
        self.USERNAME = self.get_inform(user_id)
        print('Bot was created')

    def get_inform_1(self, user_id): #словарь с атрибутами для меня
        url = f'https://api.vk.com/method/users.get?user_ids={user_id}&fields=bdate,sex,city,relation&access_token={user_token}&v=5.131'
        repl = requests.get(url)
        response = repl.json()
        information_dict = response['response']
        return information_dict

    # def find_city(self, user_id): #функция для поиска города, в словарь
    #     url = f'https://api.vk.com/method/users.get?fields=city'
    #     params = {'access_token': user_token, 'user_ids': user_id, 'v': '5.131'}
    #     repl = requests.get(url, params=params)
    #     response = repl.json()
    #     information_dict = response['response']
    #     for i in information_dict:
    #         for key, value in i.items():
    #             if key == 'city':
    #                 dict_city =i.get('city')
    #     return dict_city
    #
    # def city_id(self, user_id): #SEARCHING ID CITY
    #     dict = bot.find_city(user_id)
    #     return str(dict.get('id'))
    #
    # def city_name(self, user_id): #SEARCHING CITY NAME
    #     dict = bot.find_city(user_id)
    #     return dict.get('title')




    def get_inform(self, user_id): #Имя и фамилия входного пользователя
        url = f'https://api.vk.com/method/users.get?fields=bdate,sex,city,relation'
        params = {'access_token': user_token, 'user_ids': user_id, 'v': '5.131'}
        repl = requests.get(url, params=params)
        response = repl.json()
        information_dict = response['response']
        for i in information_dict:
            for key, value in i.items():
                first_name = i.get('first_name')
                last_name = i.get('last_name')
                bdate = i.get('bdate')
                sex = i.get('sex')
                relation = i.get('relation')
        return (f'Пользователь |{first_name} {last_name}| найден.')

    def name(self, user_id):
        url = f'https://api.vk.com/method/users.get'
        params = {'access_token': user_token, 'user_ids': user_id, 'v': '5.131'}
        repl = requests.get(url, params=params)
        response = repl.json()
        information_dict = response['response']
        for i in information_dict:
            for key, value in i.items():
                first_name = i.get('first_name')
                last_name = i.get('last_name')
                return first_name

    # def get_photo(self):
    #     url = f'https://api.vk.com/method/users.get&photo_200'
    #     params = {'access_token': user_token, 'user_ids': user_id, 'v': '5.131'}
    #     repl = requests.get(url, params=params)
    #     return repl


    # def get_age(self,user_id):
    #     url = url = f'https://api.vk.com/method/users.get?fields=bdate'
    #     params = {'access_token': user_token, 'user_ids': user_id, 'v': '5.131'}
    #     repl = requests.get(url, params=params)
    #     response = repl.json()
    #     information_list = response['response']
    #     for i in information_list:
    #         date =  i.get('bdate')# Mehod is complited
    #         date_list = date.split('.')
    #         year = int(date_list[2])
    #         year_now = datetime.date.today().year
    #         return year_now - year

    def get_sex(self, user_id):
        url = f'https://api.vk.com/method/users.get?fields=sex'
        params = {'access_token': user_token, 'user_ids': user_id, 'v': '5.131'}
        repl = requests.get(url, params=params)
        response = repl.json()
        information_list = response['response']
        for i in information_list:
            if i.get('sex') == 2:
                find_sex = 1
                return find_sex
            elif i.get('sex') == 1:
                find_sex = 2
                return find_sex

    # def getget(self):
    #     url = f'https://api.vk.com/method/users.search'
    #     params = {'access_token': user_token,
    #               'v': '5.131', 'sex' : sex(self),
    #               'age_from': age_from(self),
    #               'age_to': age_to(self),
    #               'status': '1' or '6' }
    #     resp = requests.get(url, params=params)
    #     resp_json = resp.json()
    #     return resp_json

    def foo(self):
        print(bot.find_city('342034365'))

    def get_city(self):
        url = f'https://api.vk.com/method/database.getCitiesById'
        params = {'access_token' : user_token,
                  'v': '5.131'}
        resp = requests.get(url, params=params)
        resp_json = resp.json()
        return resp_json

    def get_id(self):
        url = 'https://api.vk.com/method/utils.resolveScreenName'
        params = {'access_token' : user_token,
                  'v': '5.131',
                  'screen_name': 'heavenyoung'}
        resp = requests.get(url, params=params)
        resp_json = resp.json()
        return resp_json

    # def find_user(self): #ГОТОВО
    #     url = f'https://api.vk.com/method/users.search?fields=id,domain'
    #     params = {'access_token': user_token,
    #               'v': '5.131', 'sex': 1,
    #               'age_from': 16, 'age_to': 17,
    #               'city' : '33', #ТЕПЕРЬ НУЖНО РАЗОБРАТЬСЯ С ID ГОРОДОВ!
    #               'status': '1' or '6'}
    #     resp = requests.get(url, params=params)
    #     resp_json = resp.json()
    #     #return resp_json
    #     dict_1 = resp_json['response']
    #     list_1 = dict_1['items']
    #     for person_dict in list_1:
    #         print('vk.com/id' + str(person_dict.get('id')))




#------------------------------------------------------------------------------#

vk = vk_api.VkApi(token=comm_token) # Авторизуемся как сообщество
longpoll = VkLongPoll(vk) # Работа с сообщениями

def write_msg(user_id, message): #метод для отправки сообщения
    vk.method('messages.send', {'user_id': user_id,
                                'message': message,
                                'random_id': randrange(10 ** 7)})

def name(user_id):
    url = f'https://api.vk.com/method/users.get'
    params = {'access_token': user_token, 'user_ids': user_id, 'v': '5.131'}
    repl = requests.get(url, params=params)
    response = repl.json()
    information_dict = response['response']
    for i in information_dict:
        for key, value in i.items():
            first_name = i.get('first_name')
            last_name = i.get('last_name')
            return first_name

def get_sex(user_id):
    url = f'https://api.vk.com/method/users.get?fields=sex'
    params = {'access_token': user_token, 'user_ids': user_id, 'v': '5.131'}
    repl = requests.get(url, params=params)
    response = repl.json()
    information_list = response['response']
    for i in information_list:
        if i.get('sex') == 2:
            find_sex = 1
            return find_sex
        elif i.get('sex') == 1:
            find_sex = 2
            return find_sex

def get_age(user_id):
    url = url = f'https://api.vk.com/method/users.get?fields=bdate'
    params = {'access_token': user_token, 'user_ids': user_id, 'v': '5.131'}
    repl = requests.get(url, params=params)
    response = repl.json()
    information_list = response['response']
    for i in information_list:
        date =  i.get('bdate')# Mehod is complited
        date_list = date.split('.')
        year = int(date_list[1])
        year_now = datetime.date.today().year
    return date

def find_city(user_id):
    url = f'https://api.vk.com/method/users.get?fields=city'
    params = {'access_token': user_token, 'user_ids': user_id, 'v': '5.131'}
    repl = requests.get(url, params=params)
    response = repl.json()
    information_dict = response['response']
    for i in information_dict:
        for key, value in i.items():
            if key == 'city':
                dict_city =i.get('city')
    return dict_city

def city_id(user_id): #SEARCHING ID CITY
    dict = find_city(user_id)
    return str(dict.get('id'))

def age_from(user_id):
    write_msg(user_id, 'Введите нижнюю границу возраста искомого человека: ')
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            if event.to_me:
                age_from = event.text
                return age_from
                write_msg(user_id, f'Нижняя граница - {age_from}')


def age_to(user_id):
    write_msg(user_id, 'Введите верхнюю границу возраста искомого человека: ')
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            if event.to_me:
                age_to = event.text
                return age_to
                write_msg(user_id, f'Верхняя граница - {age_to}')

def find_user(user_id):
    url = f'https://api.vk.com/method/users.search'
    params = {'access_token': user_token,
              'v': '5.131',
              'sex' : get_sex(user_id),
              'age_from': age_from(user_id),
              'age_to': age_to(user_id),
              'status': '1' or '6'
              }
    resp = requests.get(url, params=params)
    resp_json = resp.json()
    return resp_json

def get_photo(user_id):
    url = f'https://api.vk.com/method/users.get'
    params = {'access_token': user_token,
              'user_ids': user_id,
              'v': '5.131',
              'fields': 'photo_id'
              }
    repl = requests.get(url, params=params)
    return repl

def find_user(user_id):
    url = f'https://api.vk.com/method/users.search?fields=id,domain'
    params = {'access_token': user_token,
                'v': '5.131',
                'sex': get_sex(user_id),
                'age_from': get_age(user_id),
                'age_to': get_age(user_id),
                'city' : city_id(user_id), #ТЕПЕРЬ НУЖНО РАЗОБРАТЬСЯ С ID ГОРОДОВ!
                'status': '1' or '6'}
    resp = requests.get(url, params=params)
    resp_json = resp.json()
    #return resp_json
    dict_1 = resp_json['response']
    list_1 = dict_1['items']
    for person_dict in list_1:
        return ('vk.com/id' + str(person_dict.get('id')))








bot = VKBot('342034365')
# print(bot.get_inform('342034365'))
# pprint(bot.getget())
# pprint(bot.get_inform_1('342034365'))
# print(bot.find_city('342034365'))
# print(bot.city_id('342034365'))
# print(bot.city_name('342034365'))
# print(bot.age_from())
# print(bot.age_to())
# print(bot.getget())
#print(bot.get_city())

# print(bot.get_sex('342034365'))
# print(bot.city_id('342034365'))
# print(bot.get_age('342034365'))
# print(bot.name('342034365'))






def age_from():
    write_msg('342034365', 'Введите нижнуюю границу возраста искомого человека: ')
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            if event.to_me:
                age_from = event.text
                write_msg(event.user_id, f'Нижняя граница - {age_from}')
                return age_from

def age_to():
    write_msg('342034365', 'Введите верхнюю границу возраста искомого человека: ')
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            if event.to_me:
                age_to = event.text
                write_msg(event.user_id, f'Верхняя граница - {age_to}')
                return age_to



