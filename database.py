import mysql.connector


def create_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="tasks"
    )
    if connection.is_connected():
        print('Prawidlowe polaczenie z baza danych')
    return connection
