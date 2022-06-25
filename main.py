from config import user_token, comm_token, offset, line
import vk_api
import requests
import datetime
from vk_api.longpoll import VkLongPoll, VkEventType

from random import randrange
from database import *

vk = vk_api.VkApi(token=comm_token)  # АВТОРИЗАЦИЯ СООБЩЕСТВА
longpoll = VkLongPoll(vk)  # РАБОТА С СООБЩЕНИЯМИ


def write_msg(user_id, message):
    """МЕТОД ДЛЯ ОТПРАВКИ СООБЩЕНИЙ"""
    vk.method('messages.send', {'user_id': user_id,
                                'message': message,
                                'random_id': randrange(10 ** 7)})


def name(user_id):
    """ПОЛУЧЕНИЕ ИМЕНИ ПОЛЬЗОВАТЕЛЯ, КОТОРЫЙ НАПИСАЛ БОТУ"""
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
            return first_name


def get_sex(user_id):
    """ПОЛУЧЕНИЕ ПОЛА ПОЛЬЗОВАТЕЛЯ, МЕНЯЕТ НА ПРОТИВОПОЛОЖНЫЙ"""
    url = f'https://api.vk.com/method/users.get'
    params = {'access_token': user_token,
              'user_ids': user_id,
              'fields': 'sex',
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


def get_age_low(user_id):
    """ПОЛУЧЕНИЕ ВОЗРАСТА ПОЛЬЗОВАТЕЛЯ ИЛИ НИЖНЕЙ ГРАНИЦЫ ДЛЯ ПОИСКА"""
    url = url = f'https://api.vk.com/method/users.get?fields=bdate'
    params = {'access_token': user_token,
              'user_ids': user_id,
              'fields': 'bdate',
              'v': '5.131'}
    repl = requests.get(url, params=params)
    response = repl.json()
    information_list = response['response']
    for i in information_list:
        date = i.get('bdate')
    date_list = date.split('.')
    if len(date_list) == 3:
        year = int(date_list[2])
        year_now = int(datetime.date.today().year)
        return year_now - year
    elif len(date_list) == 2 or date not in information_list:
        write_msg(user_id, 'Введите нижний порог возраста: ')
        for event in longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                age = event.text
                return age


def get_age_high(user_id):
    """ПОЛУЧЕНИЕ ВОЗРАСТА ПОЛЬЗОВАТЕЛЯ ИЛИ ВЕРХНЕЙ ГРАНИЦЫ ДЛЯ ПОИСКА"""
    url = url = f'https://api.vk.com/method/users.get'
    params = {'access_token': user_token,
              'user_ids': user_id,
              'fields': 'bdate',
              'v': '5.131'}
    repl = requests.get(url, params=params)
    response = repl.json()
    information_list = response['response']
    for i in information_list:
        date = i.get('bdate')
    date_list = date.split('.')
    if len(date_list) == 3:
        year = int(date_list[2])
        year_now = int(datetime.date.today().year)
        return year_now - year
    elif len(date_list) == 2 or date not in information_list:
        write_msg(user_id, 'Введите верхний порог возраста: ')
        for event in longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                age = event.text
                return age


def cities(user_id, city_name):
    """ПОЛУЧЕНИЕ ID ГОРОДА ПОЛЬЗОВАТЕЛЯ ПО НАЗВАНИЮ"""
    url = url = f'https://api.vk.com/method/database.getCities'
    params = {'access_token': user_token,
              'country_id': 1,
              'q': f'{city_name}',
              'need_all': 0,
              'count': 1000,
              'v': '5.131'}
    repl = requests.get(url, params=params)
    response = repl.json()
    information_list = response['response']
    list_cities = information_list['items']
    for i in list_cities:
        found_city_name = i.get('title')
        if found_city_name == city_name:
            found_city_id = i.get('id')
            return int(found_city_id)


def find_city(user_id):
    """ПОЛУЧЕНИЕ ИНФОРМАЦИИ О ГОРОДЕ ПОЛЬЗОВАТЕЛЯ"""
    url = f'https://api.vk.com/method/users.get?fields=city'
    params = {'access_token': user_token,
              'user_ids': user_id,
              'v': '5.131'}
    repl = requests.get(url, params=params)
    response = repl.json()
    information_dict = response['response']
    # return information_dict
    for i in information_dict:
        if 'city' in i:
            city = i.get('city')
            id = str(city.get('id'))
            return id
        elif 'city' not in i:
            write_msg(user_id, 'Нажми на кнопку "Начать поиск"')
            for event in longpoll.listen():
                if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                    write_msg(user_id, 'Введите название вашего города: ')
                    for event in longpoll.listen():
                        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                            city_name = event.text
                            id_city = cities(user_id, city_name)
                            if id_city != '' or id_city != None:
                                return str(id_city)
                            else:
                                break


def find_user(user_id):
    """ПОИСК ЧЕЛОВЕКА ПО ПОЛУЧЕННЫМ ДАННЫМ"""
    url = f'https://api.vk.com/method/users.search'
    params = {'access_token': user_token,
              'v': '5.131',
              'sex': get_sex(user_id),
              'age_from': get_age_low(user_id),
              'age_to': get_age_high(user_id),
              'city': find_city(user_id),
              'fields': 'is_closed',
              'fields': 'id',
              'fields': 'first_name',
              'fields': 'last_name',
              'status': '1' or '6',
              'count': 100}
    resp = requests.get(url, params=params)
    resp_json = resp.json()
    dict_1 = resp_json['response']
    list_1 = dict_1['items']
    for person_dict in list_1:
        if person_dict.get('is_closed') == False:
            first_name = person_dict.get('first_name')
            last_name = person_dict.get('last_name')
            vk_id = str(person_dict.get('id'))
            vk_link = 'vk.com/id' + str(person_dict.get('id'))
            insert_data_users(first_name, last_name, vk_id, vk_link)
        else:
            continue
    return f'Поиск завершён'


def get_photos_id(user_id):
    """ПОЛУЧЕНИЕ ID ФОТОГРАФИЙ С РАНЖИРОВАНИЕМ В ОБРАТНОМ ПОРЯДКЕ"""
    url = 'https://api.vk.com/method/photos.getAll'
    params = {'access_token': user_token,
              'type': 'album',
              'owner_id': user_id,
              'extended': 1,
              'count': 25,
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
    """ПОЛУЧЕНИЕ ID ФОТОГРАФИИ № 1"""
    list = get_photos_id(user_id)
    count = 0
    for i in list:
        count += 1
        if count == 1:
            return i[1]


def get_photo_2(user_id):
    """ПОЛУЧЕНИЕ ID ФОТОГРАФИИ № 2"""
    list = get_photos_id(user_id)
    count = 0
    for i in list:
        count += 1
        if count == 2:
            return i[1]


def get_photo_3(user_id):
    """ПОЛУЧЕНИЕ ID ФОТОГРАФИИ № 3"""
    list = get_photos_id(user_id)
    count = 0
    for i in list:
        count += 1
        if count == 3:
            return i[1]

def send_photo_1(user_id, message, offset):
    vk.method("messages.send", {"user_id": user_id,
                                'access_token': user_token,
                                'message': message,
                                'attachment': f'photo{person_id(offset)}_{get_photo_1(person_id(offset))}',
                                "random_id": 0})

def send_photo_2(user_id, message, offset):
    vk.method("messages.send", {"user_id": user_id,
                                'access_token': user_token,
                                'message': message,
                                'attachment': f'photo{person_id(offset)}_{get_photo_2(person_id(offset))}',
                                "random_id": 0})

def send_photo_3(user_id, message, offset):
    vk.method("messages.send", {"user_id": user_id,
                                'access_token': user_token,
                                'message': message,
                                'attachment': f'photo{person_id(offset)}_{get_photo_3(person_id(offset))}',
                                "random_id": 0})

def find_persons(user_id, offset):
    write_msg(user_id, found_person_info(offset))
    person_id(offset)
    #insert_data_seen_users(person_id(offset), offset )
    get_photos_id(person_id(offset))
    send_photo_1(user_id, 'Фото номер 1', offset)
    if get_photo_2(person_id(offset)) != None:
        send_photo_2(user_id, 'Фото номер 2', offset)
        send_photo_3(user_id, 'Фото номер 3', offset)
    else:
        write_msg(user_id, f'Больше фотографий нет')

def found_person_info(offset):
    """ВЫВОД ИНФОРМАЦИИ О НАЙДЕННОМ ПОЛЬЗОВАТЕЛИ"""
    tuple = select(offset)
    list = []
    for i in tuple:
        list.append(i)
    return f'{list[0]} {list[1]}, ссылка - {list[3]}'


def person_id(offset):
    """ВЫВОД ID НАЙДЕННОГО ПОЛЬЗОВАТЕЛЯ"""
    tuple = select(offset)
    list = []
    for i in tuple:
        list.append(i)
    return str(list[2])
