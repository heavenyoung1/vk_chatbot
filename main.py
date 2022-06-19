import vk_api
import requests
import datetime
from vk_api.longpoll import VkLongPoll, VkEventType
from config import user_token
from config import comm_token
from random import randrange
import json
from pprint import pprint
from database import *

class VKBot():
    def __init__(self, user_id):
        self.user_id = user_id
        # self.USERNAME = self.get_inform(user_id)
        print('Bot was created')

    # def get_inform_1(self, user_id): #словарь с атрибутами для меня
    #     url = f'https://api.vk.com/method/users.get?user_ids={user_id}&fields=bdate,sex,city,relation&access_token={user_token}&v=5.131'
    #     repl = requests.get(url)
    #     response = repl.json()
    #     information_dict = response['response']
    #     return information_dict

    # def find_city(self, user_id):  # функция для поиска города, в словарь
    #     url = f'https://api.vk.com/method/users.get?fields=city'
    #     params = {'access_token': user_token,
    #               'user_ids': user_id,
    #               'v': '5.131'}
    #     repl = requests.get(url, params=params)
    #     response = repl.json()
    #     information_dict = response['response']
    #     for i in information_dict:
    #         for key, value in i.items():
    #             if key == 'city':
    #                 dict_city = i.get('city')
    #     return dict_city

    # def city_id(self, user_id):  # SEARCHING ID CITY
    #     dict = bot.find_city(user_id)
    #     return str(dict.get('id'))
    #
    # def city_name(self, user_id):  # SEARCHING CITY NAME
    #     dict = bot.find_city(user_id)
    #     return dict.get('title')

    def name(self, user_id):
        url = f'https://api.vk.com/method/users.get'
        params = {'access_token': user_token,
                  'user_ids': user_id,
                  'v': '5.131'}
        repl = requests.get(url, params=params)
        response = repl.json()
        information_dict = response['response']
        for i in information_dict:
            for key, value in i.items():
                first_name = i.get('first_name')
                last_name = i.get('last_name')
            return first_name

    def get_age(self,user_id):
        url = url = f'https://api.vk.com/method/users.get?fields=bdate'
        params = {'access_token': user_token, 'user_ids': user_id, 'v': '5.131'}
        repl = requests.get(url, params=params)
        response = repl.json()
        information_list = response['response']
        for i in information_list:
            date =  i.get('bdate')# Mehod is complited
            date_list = date.split('.')
            year = int(date_list[2])
            year_now = datetime.date.today().year
            return year_now - year

    def get_sex(self, user_id):
        url = f'https://api.vk.com/method/users.get?fields=sex'
        params = {'access_token': user_token,
                  'user_ids': user_id,
                  'v': '5.131'}
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

    # def find_user(self, user_id):  # ГОТОВО
    #     url = f'https://api.vk.com/method/users.search?fields=id,domain,first_name,last_name'
    #     params = {'access_token': user_token,
    #               'v': '5.131', 'sex': 1,
    #               'age_from': 25, 'age_to': 35,
    #               'city': '33',
    #               'status': '1' or '6',
    #               'count': 100}
    #     resp = requests.get(url, params=params)
    #     resp_json = resp.json()
    #     # return resp_json
    #     dict_1 = resp_json['response']
    #     list_1 = dict_1['items']
    #     information = []
    #     drop()
    #     create_table()
    #     for person_dict in list_1:
    #         first_name = person_dict.get('first_name')
    #         last_name = person_dict.get('last_name')
    #         vk_id = str(person_dict.get('id'))
    #         vk_link = 'https://vk.com/id' + str(person_dict.get('id'))
    #         insert_data(first_name, last_name, vk_id, vk_link)
    #     return f'Поиск завершён'


    def get_photos_id(self, user_id):
        url = 'https://api.vk.com/method/photos.getAll'
        params = {'access_token': user_token,
                  'type' : 'album',
                  'owner_id' : '328116348',
                  'extended': 1,
                  'count' : 3,
                  'v': '5.131'}
        resp = requests.get(url, params=params)
        dict_photos = dict()
        resp_json = resp.json()
        dict_1 = resp_json['response']
        list_1 = dict_1['items']
        for i in list_1:
            photo_id = str(i.get('id'))
            i_likes = i.get('likes')
            if i_likes.get('count'):
                likes = i_likes.get('count')
                dict_photos[likes] = photo_id
        list_of_ids = sorted(dict_photos.items(), reverse=True)
        return list_of_ids

    def get_photo_1(self,user_id):
        list = self.get_photos_id(user_id)
        count = 0
        for i in list:
            count += 1
            if count == 1:
                return i[1]

    def get_photo_2(self,user_id):
        list = self.get_photos_id(user_id)
        count = 0
        for i in list:
            count += 1
            if count == 2:
                return i[1]

    def get_photo_3(self,user_id):
        list = self.get_photos_id(user_id)
        count = 0
        for i in list:
            count += 1
            if count == 3:
                return i[1]




bot = VKBot('342034365')
print(bot.get_photos_id('328116348'))
print(bot.get_photo_1('328116348'))
print(bot.get_photo_2('328116348'))
print(bot.get_photo_3('328116348'))
# ------------------------------------------------------------------------------#

vk = vk_api.VkApi(token=comm_token)  # Авторизуемся как сообщество
longpoll = VkLongPoll(vk)  # Работа с сообщениями


def write_msg(user_id, message):  # метод для отправки сообщения
    vk.method('messages.send', {'user_id': user_id,
                                'message': message,
                                'random_id': randrange(10 ** 7)})


def name(user_id):
    url = f'https://api.vk.com/method/users.get'
    params = {'access_token': user_token,
              'user_ids': user_id,
              'v': '5.131'}
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
    params = {'access_token': user_token,
              'user_ids': user_id,
              'v': '5.131'}
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
        date = i.get('bdate')  # Mehod is complited
        date_list = date.split('.')
        try:
            year = int(date_list[2])
            year_now = int(datetime.date.today().year)
            return year_now - year
        except IndexError:
            write_msg(user_id, 'ERROR')

def find_city(user_id):
    url = f'https://api.vk.com/method/users.get?fields=city'
    params = {'access_token': user_token,
              'user_ids': user_id,
              'v': '5.131'}
    repl = requests.get(url, params=params)
    response = repl.json()
    information_dict = response['response']
    for i in information_dict:
        for key, value in i.items():
            if key == 'city':
                dict_city = i.get('city')
    return dict_city


def city_id(user_id):  # SEARCHING ID CITY
    dict = find_city(user_id)
    return str(dict.get('id'))

def find_user(user_id):
    url = f'https://api.vk.com/method/users.search?fields=id,domain,first_name,last_name'
    params = {'access_token': user_token,
              'v': '5.131', 'sex': get_sex(user_id),
              'age_from': get_age(user_id),
              'age_to': get_age(user_id),
              'city': city_id(user_id),
              'is_closed': False,
              'can_access_closed': True,
              #'status': '1' or '6',
              'count': 100}
    resp = requests.get(url, params=params)
    resp_json = resp.json()
    # return resp_json
    dict_1 = resp_json['response']
    list_1 = dict_1['items']
    information = []
    drop()
    create_table()
    for person_dict in list_1:
        first_name = person_dict.get('first_name')
        last_name = person_dict.get('last_name')
        vk_id = str(person_dict.get('id'))
        vk_link = 'https://vk.com/id' + str(person_dict.get('id'))
        insert_data(first_name, last_name, vk_id, vk_link)
    return f'Поиск завершён'

# found_person_info()
# person_id()

def get_photos_id(user_id):
    url = 'https://api.vk.com/method/photos.getAll'
    params = {'access_token': user_token,
              'type' : 'album',
              'owner_id' : user_id,
              'extended': 1,
              'count' : 25,
              'v': '5.131'}
    resp = requests.get(url, params=params)
    dict_photos = dict()
    resp_json = resp.json()
    dict_1 = resp_json['response']
    list_1 = dict_1['items']
    for i in list_1:
        photo_id = str(i.get('id'))
        i_likes = i.get('likes')
        if i_likes.get('count'):
            likes = i_likes.get('count')
            dict_photos[likes] = photo_id
    list_of_ids = sorted(dict_photos.items(), reverse=True)
    return list_of_ids

def get_photo_1(user_id):
    list = get_photos_id(user_id)
    count = 0
    for i in list:
        count += 1
        if count == 1:
            return i[1]

def get_photo_2(user_id):
    list = get_photos_id(user_id)
    count = 0
    for i in list:
        count += 1
        if count == 2:
            return i[1]

def get_photo_3(user_id):
    list = get_photos_id(user_id)
    count = 0
    for i in list:
        count += 1
        if count == 3:
            return i[1]
