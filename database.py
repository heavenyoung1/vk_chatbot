import psycopg2
from config import *
from pprint import pprint

connection = psycopg2.connect(
    host=host,
    user=user,
    password=password,
    database=db_name
)

connection.autocommit = True

def create_table_users():
    with connection.cursor() as cursor:
        cursor.execute(
            """CREATE TABLE users(
                id serial,
                first_name varchar(50) NOT NULL,
                last_name varchar(25) NOT NULL,
                vk_id varchar(20) NOT NULL PRIMARY KEY,
                vk_link varchar(50));"""
        )
    print("[INFO] Table USERS was created.")

# def create_table_seen_users():
#     with connection.cursor() as cursor:
#         cursor.execute(
#             """CREATE TABLE seen_users(
#             id serial,
#             vk_id varchar(50) PRIMARY KEY references users(vk_id));"""
#         )

# def insert_seen_users(vk_id):
#      with connection.cursor() as cursor:
#             cursor.execute(
#                 f"""INSERT INTO seen_users (vk_id) VALUES ('{found_vk_id(offset)}');""")

# def drop_seen_users():
#     with connection.cursor() as cursor:
#         cursor.execute(
#             """DROP TABLE seen_users;"""
#         )
#         print('[INFO] Table SEEN_USERS was deleted.')



# def insert_data():
#     with connection.cursor() as cursor:
#         cursor.execute(
#             """INSERT INTO users (first_name, last_name, vk_link) VALUES
#             ('Eugene', 'Mefyod', '12345678');"""
#         )

def insert_data(first_name, last_name, vk_id, vk_link):
    with connection.cursor() as cursor:
        cursor.execute(
            f"""INSERT INTO users (first_name, last_name, vk_id, vk_link) 
            VALUES ('{first_name}', '{last_name}', '{vk_id}', '{vk_link}');"""
        )

# def select():
#     with connection.cursor() as cursor:
#         cursor.execute(
#             """SELECT first_name, last_name, vk_id, vk_link  FROM users ORDER BY id;"""
#         )
#         return cursor.fetchone()

# def select(offset):
#     with connection.cursor() as cursor:
#         cursor.execute(
#             f"""SELECT first_name, last_name, vk_id, vk_link  FROM users
#                 ORDER BY id
#                 OFFSET '{offset}';"""
#         )
#         return cursor.fetchone()

def select(offset):
    with connection.cursor() as cursor:
        cursor.execute(
            f"""SELECT first_name, last_name, vk_id, vk_link  FROM users
                ORDER BY id
                OFFSET '{offset}';"""
        )
        return cursor.fetchone()

def found_person_info(offset):
    tuple = select(offset)
    list = []
    for i in tuple:
        list.append(i)
    return f'{list[0]} {list[1]}, ссылка - {list[3]}'

def found_vk_id(offset):
    tuple = select(offset)
    list = []
    for i in tuple:
        list.append(i)
    return f'{list[2]}'

def person_id(offset):
    tuple = select(offset)
    list = []
    for i in tuple:
        list.append(i)
    return str(list[2])


def drop():
    with connection.cursor() as cursor:
        cursor.execute(
            """DROP TABLE users;"""
        )
        print('[INFO] Table USERS was deleted.')

# drop()
# create_table()
# insert_data()
# drop()
#(select(50))
#drop_seen_users()
