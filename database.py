import mysql.connector

def create_database(cursor):
    cursor.execute("CREATE DATABASE pahrithcheese")

def create_cheese_table(cursor):

if __name__ == '__main__':
    my_db = mysql.connector.connect(
        user='root', password='Pahrithcheese!', database='pahrithcheese')
    print('connected')
    my_cursor = my_db.cursor()
    my_cursor.execute("SHOW DATABASES")

    for x in my_cursor:
        print(x)
