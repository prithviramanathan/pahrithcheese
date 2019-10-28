import mysql.connector

def create_database(cursor):
    cursor.execute("CREATE DATABASE pahrithcheese")

if __name__ == '__main__':
    my_db = mysql.connector.connect(
        host='127.0.0.1',
        user='pahrithcheese',
        passwd='Pahrithcheese!'
    )
    my_cursor = my_db.cursor()
    create_database(my_cursor)
    my_cursor.execute("SHOW DATABASES")

    for x in my_cursor:
        print(x)
