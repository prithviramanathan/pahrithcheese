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
        self.pairing = item[12]



def create_database(cursor):
    cursor.execute("CREATE DATABASE pahrithcheese")

def create_cheese_table(cursor):
    sql_string = "CREATE TABLE cheeses (name VARCHAR(50) PRIMARY KEY, description VARCHAR(1024), region VARCHAR(50),family VARCHAR(50), fat_content VARCHAR(50), color VARCHAR(50), flavor VARCHAR(50), aroma VARCHAR(50), texture VARCHAR(50), type VARCHAR(50), country_of_origin VARCHAR(50), image VARCHAR(255))"
    cursor.execute(sql_string)

def create_pairings_table(cursor):
    sql_string = "CREATE TABLE pairings (name VARCHAR(50), recipe VARCHAR(1024))"
    cursor.execute(sql_string)

def create_likes_table(cursor):
    sql_string = "CREATE TABLE likes (email VARCHAR(50), cheese VARCHAR(50))"
    cursor.execute(sql_string)

def create_friends_table(cursor):
    sql_string = "CREATE TABLE friends (email1 VARCHAR(50), email2 VARCHAR(50))"
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
    return [vars(Cheese(x)) for x in result]


def update_pairings(cursor, db, cheese, recipe):
    sql_string = "UPDATE pairings SET recipe = '" + recipe + "' WHERE name = '" + cheese + "'"
    cursor.execute(sql_string)
    db.commit()

# toggles the friendship status for a friend (email2)
def add_friend(cursor, db, email1, email2):
    sql = 'SELECT * FROM friends WHERE email1 = "' + email1 + '" AND email2 = "' + email2 + '"'
    cursor.execute(sql)
    result = cursor.fetchall()
    if len(result) == 0:
        print('adding friend')
        sql = 'INSERT INTO friends (email1, email2) values (%s, %s)'
        val = (email1, email2)
        cursor.execute(sql, val)
        db.commit()
        return 'added a friend'
    else:
        print('removing friend')
        sql = 'DELETE FROM friends WHERE email1 = "' + email1 + '" AND email2 = "' + email2 + '"'
        cursor.execute(sql)
        db.commit()
        return 'removed friend'



def create_stored_procedure_likes(cursor, db):
    sql = """
    CREATE PROCEDURE ToggleLike(
      IN c VARCHAR(50),
      IN e VARCHAR(50)
    )
        BEGIN
            IF EXISTS (SELECT * FROM likes WHERE cheese = c AND email = e)
                DELETE FROM likes WHERE cheese = c AND email = e;
            ELSE
                INSERT INTO likes (email, cheese) VALUES (e, c);
        END //
    DELIMITER ;
    """
    cursor.execute(sql)
    db.commit()

def like_cheese(cursor, db, email, cheese):
    sql = 'EXEC ToggleLike @Cheese = "' + cheese + '", @Email = "' + email + '"'
    cursor.execute(sql)
    db.commit()
    return "toggled like"


def get_my_likes(cursor, email):
    sql = 'SELECT cheese FROM likes WHERE email = "' + email + '";'
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

def get_my_friends(cursor, email):
    sql = 'SELECT email2 FROM friends WHERE email1 = "' + email + '"'
    cursor.execute(sql)
    result = cursor.fetchall()
    return result


def format_shared(list):
    retval = {}
    for elem in list:
        if elem[0] not in retval:
            retval[elem[0]] = []
        retval[elem[0]].append(elem[1])


def shared_preferences(cursor, email):
    sql = 'SELECT l.cheese, f.email2 FROM likes l JOIN friends f ON l.email = f.email1 WHERE l.email = "' + email + '" AND l.cheese IN (SELECT cheese from likes l2 WHERE l2.email = f.email2)'
    cursor.execute(sql)
    result = cursor.fetchall()
    result = format_shared(result)
    return result




def get_user_profile(cursor, email):
    friends = get_my_friends(cursor, email)
    cheeses =  get_my_likes(cursor, email)
    friend_shared_cheeses = shared_preferences(cursor, email)
    for i in range(len(friends)):
        friends[i] = friends[i][0]
    for i in range(len(cheeses)):
        cheeses[i] = cheeses[i][0]
    return {'friends': friends, 'liked cheeses': cheeses, 'email': email, 'friends who share interests': friend_shared_cheeses}



if __name__ == '__main__':
    my_db = mysql.connector.connect(
        user='root', password='Pahrithcheese!', database='pahrithcheese')
    my_cursor = my_db.cursor()
    #create_cheese_table(my_cursor)
    #create_pairings_table(my_cursor)
    #fill_cheese_table(my_cursor, my_db)
    #fill_pairings_table(my_cursor, my_db)
    #print('inserted elements')
    # update_pairings(my_cursor, my_db, 'Abbaye de Belloc', '')
    # print(search_cheeses(my_cursor, 'Abbaye de Belloc').recipe)
    # create_likes_table(my_cursor)
    # create_friends_table(my_cursor)
    # create_stored_procedure_likes(my_cursor, my_db)
