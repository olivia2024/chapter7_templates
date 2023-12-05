from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    """Index URL"""
    return render_template('index.html', Title='Index page')

@app.route('/about_me')
def about_me():
    """About me URL"""
    return render_template('about_me.html', title='About Me Page')