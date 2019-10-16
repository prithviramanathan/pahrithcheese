from flask import Flask
app = Flask(__name__)

# Search for a cheese
@app.route('/search', methods=['GET'])
def search():
    return 'no results'

# add a friend
@app.route('/add_friend', methods=['POST'])
def add_friend():
    return 'added friend'

# add a cheese to favorites
@app.route('/add_favorite', methods=['POST'])
def add_cheese_to_favorites():
    return 'added cheese to favorites'

if __name__ == '__main__':
    app.run()
