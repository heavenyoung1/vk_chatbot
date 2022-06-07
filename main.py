import vk_api
import requests
from config import user_token
from config import comm_token
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

    def find_city(self, user_id): #функция для поиска города, в словарь
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

    def city_id(self, user_id): #SEARCHING ID CITY
        dict = bot.find_city(user_id)
        return dict.get('id')

    def city_name(self, user_id): #SEARCHING CITY NAME
        dict = bot.find_city(user_id)
        return dict.get('title')





    def get_inform(self, user_id):
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

    def input_infrom(self, user_id):
        print('''Добро Пожаловать в Бот VKinder. 
                 Мы найдём вам пару, вам нужно ввести информацию, которая будет указана далее. 
                 Мы имщем для вас пару с Семейным положением -
                 |Незамужем|, |Неженат|, |В активном поиске|.''')
        old = int(input('Введите возраст: '))
        sex_str = str(input('Введите пол человека, |М| или |Ж|: '))
        if sex_str == 'Ж' or sex_str == 'ж':
            sex = 1
        elif sex_str == 'М' or sex_str == 'м' or sex_str == 'M' or sex_str == 'm':
            sex = 2
        else:
            print('Некорректный ввод.')
        print(f'Мы ищем для вас пару возрастом от {old - 2} до {old + 2} лет, в городе |{bot.city_name(user_id)}|. ')



    def getget(self):
        url = f'https://api.vk.com/method/users.search'
        params = {'access_token': user_token,'v': '5.131', 'sex' : 2, 'age_from': '30', 'age_to': '40', 'status': '1' or '6' }
        resp = requests.get(url, params=params)
        resp_json = resp.json()
        return resp_json

    def foo(self):
        print(bot.find_city('342034365'))


bot = VKBot('342034365')
# print(bot.get_inform('342034365'))
# pprint(bot.getget())
# pprint(bot.get_inform_1('342034365'))
bot.input_infrom('342034365')
print(bot.find_city('342034365'))
print(bot.city_id('342034365'))
print(bot.city_name('342034365'))







