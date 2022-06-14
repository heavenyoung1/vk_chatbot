import psycopg2


from config import *

connection = psycopg2.connect(
    host=host,
    user=user,
    password=password,
    database=db_name
)

connection.autocommit = True


def create_table():
    with connection.cursor() as cursor:
        cursor.execute(
            """CREATE TABLE users(
                id serial,
                first_name varchar(50) NOT NULL,
                last_name varchar(50) NOT NULL,
                vk_id varchar(75) NOT NULL,
                vk_link varchar(75) PRIMARY KEY);"""
        )
    print("[INFO] Table was created.")


# def insert_data():
#     with connection.cursor() as cursor:
#         cursor.execute(
#             """INSERT INTO users (first_name, last_name, vk_link) VALUES
#             ('Eugene', 'Mefyod', '12345678');"""
#         )

def insert_data(first_name, last_name, vk_id, vk_link):
    with connection.cursor() as cursor:
        cursor.execute(
            f"""INSERT INTO users (first_name, last_name, vk_id, vk_link) VALUES
            ('{first_name}', '{last_name}', '{vk_id}', '{vk_link}');"""
        )

def select():
    with connection.cursor() as cursor:
        cursor.execute(
            """SELECT id, first_name, last_name, vk_link  FROM users;"""
        )
        return cursor.fetchall()


def drop():
    with connection.cursor() as cursor:
        cursor.execute(
            """DROP TABLE users;"""
        )
        print('[INFO] Table was deleted.')

# drop()
# create_table()
# insert_data()
# drop()

