from flask import Flask, request
import json
import flask
from database import *
from pymongo import MongoClient

app = Flask(__name__)
db = mysql.connector.connect(
    user='root', password='Pahrithcheese!', database='pahrithcheese')
cursor = db.cursor()
client = MongoClient(port=27017)
mongodb=client.pahrithcheese




# Search for a cheese
@app.route('/search', methods=['GET'])
def search():
    cheese_name = request.args.get('cheeseName', '')
    retval = search_cheeses(cursor, mongodb, cheese_name)
    mystr = json.dumps(retval)
    resp = flask.Response(mystr)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

@app.route('/update-pairings', methods=['POST'])
def update_recipes():
    print(json.dumps(request.form))
    print(json.dumps(request.args))
    data = request.form
    mystr = ''
    try:
        update_pairings(cursor, db, data.get('cheeseName', ''), data.get('pairing', ''))
        mystr = json.dumps(search_cheeses(cursor, mongodb, data.get('cheeseName', '')))
        print('return value', mystr)
    except:
        mystr = 'Did not update'
    resp = flask.Response(mystr)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


# add a cheese to favorites
@app.route('/toggle-like', methods=['POST'])
def add_cheese_to_favorites():
    data = request.form
    mystr = ''
    if data.get('email', '') == '' or data.get('cheese', '') == '':
        mystr = json.dumps(['invalid params'])
    try:
        value = like_cheese(cursor, db, data.get('email', ''), data.get('cheese', ''))
        mystr = json.dumps([value])
    except:
        mystr = json.dumps(['failed to add cheese to favorite'])
    resp = flask.Response(mystr)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

# adds or removes a friend
@app.route('/toggle-friend', methods=['POST'])
def add_or_remove_friend():
    data = request.form
    mystr = ''
    if data.get('me', '') == '' or data.get('other_user', '') == '':
        mystr = json.dumps(['invalid params'])
    try:
        value = add_friend(cursor, db, data.get('me'), data.get('other_user'))
        mystr = json.dumps([value])
    except:
        mystr = json.dumps(['failed to add friend'])
    resp = flask.Response(mystr)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

@app.route('/get-profile', methods=['GET'])
def get_profile():
    mystr = ''
    email = request.args.get('email', '')
    try:
        mystr =  json.dumps(get_user_profile(cursor, email))

    except:
        mystr =  json.dumps(['failed to load profile'])
    resp = flask.Response(mystr)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

@app.route('/shared-preferences', methods= ['GET'])
def shared():
    email = request.args.get('email', '')
    return json.dumps(shared_preferences(cursor, email))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
