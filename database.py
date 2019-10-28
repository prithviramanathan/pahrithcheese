import mysql.connector

def create_database(cursor):
    cursor.execute("CREATE DATABASE pahrithcheese")

def create_cheese_table(cursor):
    sql_string = "CREATE TABLE cheeses" +
    "(name VARCHAR(50), description VARCHAR(1024), region VARCHAR(50)" +
    "family VARCHAR(50), fat_content VARCHAR(50), color VARCHAR(50), " +
    "flavor VARCHAR(50), aroma VARCHAR(50), texture VARCHAR(50), type VARCHAR(50)" +
    "country_of_origin VARCHAR(50))"
    my_cursor.execute(sql_string)

def create_pairings_table(cursor):
    sql_string = "CREATE TABLE pairings (name VARCHAR(50), recipe VARCHAR(1024))"
    my_cursor.execute(sql_string)

if __name__ == '__main__':
    my_db = mysql.connector.connect(
        user='root', password='Pahrithcheese!', database='pahrithcheese')
    print('connected')
    my_cursor = my_db.cursor()
    create_cheese_table(my_cursor)
    create_pairings_table(my_cursor)
    my_cursor.execute("SHOW TABLES")

    for x in my_cursor:
        print(x)
