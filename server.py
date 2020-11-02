"""Server for movie ratings app."""

#from flask import Flask
from flask import (Flask, render_template, request, flash, session,
                   redirect)
from model import connect_to_db
import crud

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def homepage():
    """View Homepage"""
    
    return render_template('homepage.html')

# Replace this with routes and view functions!

@app.route('/movies')
def get_all_movies():

    all_movies = crud.get_movies()
    return render_template('all_movies.html',movies = all_movies)

@app.route('/movies/<movie_id>')
def show_movie(movie_id):

    movie_details = crud.get_movie_by_id(movie_id)
    return render_template('movie_details.html', movie = movie_details)

@app.route('/users')
def get_all_users():

    all_users = crud.get_users()
    return render_template('all_users.html', users = all_users)

@app.route('/users/<user_id>')
def show_user(user_id):

    user_details = crud.get_user_by_id(user_id)
    return render_template('user_details.html', user = user_details)

if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)