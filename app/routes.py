from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miquel'}
    posts = [
        {
            'authour':{'username':'John'},
            'body': 'Beautiful day in Protland!'
        },
        {
            'authour': {'username': 'Susan'},
            'body': 'Beautiful day in so cool!'
        }
    ]
    return render_template('index.html',title='Home', user=user, posts=posts)
