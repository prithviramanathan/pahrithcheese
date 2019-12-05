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

# add a cheese to favorites
@app.route('/toggle-like', methods=['POST'])
def add_cheese_to_favorites():
    data = request.form
    if data.get('email', '') == '' or data.get('cheese', '') == '':
        return 'invalid params'
    try:
        value = like_cheese(cursor, db, data.get('email', ''), data.get('cheese', ''))
        return value
    except:
        return 'failed to add cheese to favorite'

# adds or removes a friend
@app.route('/toggle-friend', methods=['POST'])
def add_or_remove_friend():
    data = request.form
    if data.get('me', '') == '' or data.get('other_user', '') == '':
        return 'invalid params'
    try: 
        value = add_friend(cursor, db, data.get('me'), data.get('other_user'))
        return value
    except:
        return 'failed to add friend'

@app.route('/get-profile', methods=['GET'])
def get_profile():
    email = request.args.get('email', '')
    try:
        return json.dumps(get_user_profile(cursor, email))
    except:
        print('failed to load profile')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
