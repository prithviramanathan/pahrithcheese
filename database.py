import mysql.connector
import json
def create_database(cursor):
    cursor.execute("CREATE DATABASE pahrithcheese")

def create_cheese_table(cursor):
    sql_string = "CREATE TABLE cheeses (name VARCHAR(50) PRIMARY KEY, description VARCHAR(1024), region VARCHAR(50),family VARCHAR(50), fat_content VARCHAR(50), color VARCHAR(50), flavor VARCHAR(50), aroma VARCHAR(50), texture VARCHAR(50), type VARCHAR(50), country_of_origin VARCHAR(50), image VARCHAR(255))"
    cursor.execute(sql_string)

def create_pairings_table(cursor):
    sql_string = "CREATE TABLE pairings (name VARCHAR(50), recipe VARCHAR(1024))"
    cursor.execute(sql_string)


def fill_cheese_table(cursor, db):
    sql = "INSERT INTO cheeses (name, description, region, family, fat_content, color, flavor, aroma, texture, type, country_of_origin, image) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    vals = []
    data = None
    with open('cheese.json') as f:
        data = json.load(f)
    cheeses = set([])
    for item in data:
        if item['name'] in cheeses:
            continue
        cheeses.add(item['name'])
        val = (item.get('name', None), item.get('description', None), item.get('region', None), item.get('family', None), item.get('fat_content', None), item.get('colour', None), item.get('flavour', None), item.get('aroma', None), item.get('texture', None), item.get('type', None), item.get('country_of_origin', None), item.get('image', None))
        cursor.execute(sql, val)
        db.commit()
        print('inserted an item')                                                               
if __name__ == '__main__':
    my_db = mysql.connector.connect(
        user='root', password='Pahrithcheese!', database='pahrithcheese')
    my_cursor = my_db.cursor()
    #create_cheese_table(my_cursor)
    #create_pairings_table(my_cursor)
    #fill_cheese_table(my_cursor, my_db)
    #print('inserted elements')
    my_cursor.execute('SELECT COUNT(*) FROM cheeses')
    for x in my_cursor:
        print(x)
