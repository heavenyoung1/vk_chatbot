import psycopg2
from config import *

connection = psycopg2.connect(
    host=host,
    user=user,
    password=password,
    database=db_name
)

connection.autocommit = True


def create_table_users():
    """СОЗДАНИЕ ТАБЛИЦЫ USERS (НАЙДЕННЫЕ ПОЛЬЗОВАТЕЛИ"""
    with connection.cursor() as cursor:
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS users(
                id serial,
                first_name varchar(50) NOT NULL,
                last_name varchar(25) NOT NULL,
                vk_id varchar(20) NOT NULL PRIMARY KEY,
                vk_link varchar(50));"""
        )
    print("[INFO] Table USERS was created.")


def create_table_seen_users():  # references users(vk_id)
    """СОЗДАНИЕ ТАБЛИЦЫ SEEN_USERS (ПРОСМОТРЕННЫЕ ПОЛЬЗОВАТЕЛИ"""
    with connection.cursor() as cursor:
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS seen_users(
            id serial,
            vk_id varchar(50) PRIMARY KEY);"""
        )
    print("[INFO] Table SEEN_USERS was created.")


def insert_data_users(first_name, last_name, vk_id, vk_link):
    """ВСТАВКА ДАННЫХ В ТАБЛИЦУ USERS"""
    with connection.cursor() as cursor:
        cursor.execute(
            f"""INSERT INTO users (first_name, last_name, vk_id, vk_link) 
            VALUES ('{first_name}', '{last_name}', '{vk_id}', '{vk_link}');"""
        )


def insert_data_seen_users(vk_id, offset):
    """ВСТАВКА ДАННЫХ В ТАБЛИЦУ SEEN_USERS"""
    with connection.cursor() as cursor:
        cursor.execute(
            f"""INSERT INTO seen_users (vk_id) 
            VALUES ('{vk_id}')
            OFFSET '{offset}';"""
        )


def select(offset):
    """ВЫБОРКА ИЗ НЕПРОСМОТРЕННЫХ ЛЮДЕЙ"""
    with connection.cursor() as cursor:
        cursor.execute(
            f"""SELECT u.first_name,
                        u.last_name,
                        u.vk_id,
                        u.vk_link,
                        su.vk_id
                        FROM users AS u
                        LEFT JOIN seen_users AS su 
                        ON u.vk_id = su.vk_id
                        WHERE su.vk_id IS NULL
                        OFFSET '{offset}';"""
        )
        return cursor.fetchone()


def drop_users():
    """УДАЛЕНИЕ ТАБЛИЦЫ USERS КАСКАДОМ"""
    with connection.cursor() as cursor:
        cursor.execute(
            """DROP TABLE IF EXISTS users CASCADE;"""
        )
        print('[INFO] Table USERS was deleted.')


def drop_seen_users():
    """УДАЛЕНИЕ ТАБЛИЦЫ SEEN_USERS КАСКАДОМ"""
    with connection.cursor() as cursor:
        cursor.execute(
            """DROP TABLE  IF EXISTS seen_users CASCADE;"""
        )
        print('[INFO] Table SEEN_USERS was deleted.')


def creating_database():
    drop_users()
    drop_seen_users()
    create_table_users()
    create_table_seen_users()
