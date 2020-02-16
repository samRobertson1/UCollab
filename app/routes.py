from flask import render_template
from app import app

from app.forms import LoginForm
#>>>>>>> e2e73dc0264279f7ddb5719fa1fd05b1fd4ba19c

@app.route('/')
@app.route('/index')
def index():
    user = {'username' : 'sam'}
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
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
#>>>>>>> e2e73dc0264279f7ddb5719fa1fd05b1fd4ba19c`
