from flask import Flask, request
import json
from database import *
app = Flask(__name__)
db = mysql.connector.connect(
    user='root', password='Pahrithcheese!', database='pahrithcheese')
cursor = db.cursor()

# Search for a cheese
@app.route('/search', methods=['GET'])
def search():
    cheese_name = request.args.get('cheeseName', '')
    retval = search_cheeses(cursor, cheese_name)
    return json.dumps(retval)

@app.route('/update-pairings', methods=['POST'])
def update_recipes():
    print(json.dumps(request.form))
    print(json.dumps(request.args))
    data = request.form
    try:
        update_pairings(cursor, db, data.get('cheeseName', ''), data.get('pairing', ''))
        return json.dumps(search_cheeses(cursor, data.get('cheeseName', '')))
    except:
        return 'Did not update'

# add a friend
@app.route('/add-friend', methods=['POST'])
def add_friend():
    return 'added friend'

# add a cheese to favorites
@app.route('/add-favorite', methods=['POST'])
def add_cheese_to_favorites():
    return 'added cheese to favorites'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
