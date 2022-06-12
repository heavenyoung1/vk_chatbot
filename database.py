import  psycopg2
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
                id serial PRIMARY KEY,
                first_name varchar(50) NOT NULL,
                last_name varchar(50) NOT NULL,
                vk_link varchar(75) NOT NULL);"""
    )
    print("[INFO] Table was created.")

def inser_data():
    with connection.cursor() as cursor:
        cursor.execute(
            """INSERT INTO users (first_name, last_name, vk_id) VALUES
            ('Eugene', 'Mefyod', '12345678');"""
        )

with connection.cursor() as cursor:
    cursor.execute(
        """SELECT id, first_name, last_name, vk_id  FROM users;"""
    )
    print(cursor.fetchone())

with connection.cursor() as cursor:
    cursor.execute(
        """DROP TABLE users;"""
    )
    print('[INFO] Table was deleted.')

