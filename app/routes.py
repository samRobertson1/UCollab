from flask import render_template
from app import app
from app import mongo

@app.route('/')
@app.route('/index')
def index():
    user_collection = mongo.db.users
    user_collection.insert({'name' : 'Sam'})
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user='Sam', posts=posts)
#def index():
 #   user = {'username': 'Sam'}
  #  return render_template('index.html', title='Home', user=user)

