import mysql.connector
import json
class Cheese:
    def __init__(self, item):
        self.name = item[0]
        self.description = item[1]
        self.region = item[2]
        self.family = item[3]
        self.fat_content = item[4]
        self.color = item[5]
        self.flavor = item[6]
        self.aroma = item[7]
        self.texture = item[8]
        self.type = item[9]
        self.country_of_origin = item[10]
        self.image = item[11]
        self.recipe = item[12]



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

def fill_pairings_table(cursor, db):
    sql = "INSERT INTO pairings (name, recipe) VALUES (%s, %s)"
    data = None
    with open('cheese.json') as f:
        data = json.load(f)
    cheeses = set([])
    for item in data:
        if item['name'] in cheeses:
            continue
        cheeses.add(item['name'])
        val = (item.get('name', None), '')
        cursor.execute(sql, val)
        db.commit()

def search_cheeses(cursor, cheese):
    sql_string = 'SELECT * FROM cheeses NATURAL JOIN pairings WHERE name = "' + cheese + '"'
    cursor.execute(sql_string)
    result = cursor.fetchall()
    retval = []
    for x in result:
        retval.append(Cheese(x))
    return retval

def update_pairings(cursor, db, cheese, recipe):
    sql_string = "UPDATE pairings SET recipe = '" + recipe + "' WHERE name = '" + cheese + "'"
    cursor.execute(sql_string)
    db.commit()

"""
if __name__ == '__main__':
    my_db = mysql.connector.connect(
        user='root', password='Pahrithcheese!', database='pahrithcheese')
    my_cursor = my_db.cursor()
    #create_cheese_table(my_cursor)
    #create_pairings_table(my_cursor)
    #fill_cheese_table(my_cursor, my_db)
    #fill_pairings_table(my_cursor, my_db)
    #print('inserted elements')
    update_pairings(my_cursor, my_db, 'Abbaye de Belloc', '')
    print(search_cheeses(my_cursor, 'Abbaye de Belloc').recipe)
"""
