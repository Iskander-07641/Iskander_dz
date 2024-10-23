import psycopg2


def get_connection():

    conn = psycopg2.connect(
        dbname="ваша_база_данных",
        user="ваш_пользователь",
        password="ваш_пароль",
        host="localhost",
        port="5432"
    )
    return conn