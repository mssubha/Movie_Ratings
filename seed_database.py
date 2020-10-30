"""Script to seed database."""

import os #module from Python’s standard library, code related to working with your computer’s operating system.
import json
from random import choice, randint
from datetime import datetime #We’ll use datetime.strptime to turn a string into a Python datetime object.

import crud
import model
import server

os.system('dropdb ratings')
os.system('createdb ratings')

model.connect_to_db(server.app)
model.db.create_all()

# Load movie data from JSON file
with open('data/movies.json') as f:
    movie_data = json.loads(f.read())


# TODO: create a movie here and append it to movies_in_db
# Create movies, store them in list so we can use them
# to create fake ratings later
movies_in_db = []
for movie in movie_data:
    title = movie["title"]
    overview = movie["overview"]
    release_date  = datetime.strptime(movie["release_date"], "%Y-%m-%d")
    poster_path  = movie["poster_path"]

    add_movie = crud.create_movie(title,overview,release_date,poster_path)
    movies_in_db.append(add_movie)


    # "overview": "The near future, a time when both hope and hardships drive humanity to look to the stars and beyond. While a mysterious phenomenon menaces to destroy life on planet Earth, astronaut Roy McBride undertakes a mission across the immensity of space and its many perils to uncover the truth about a lost expedition that decades before boldly faced emptiness and silence in search of the unknown.",
    # "poster_path": "https://image.tmdb.org/t/p/original//xBHvZcjRiWyobQ9kxBhO6B2dtRI.jpg",
    # "release_date": "2019-09-20",
    # "title": "Ad Astra"

    # title, overview, release_date, poster_path

    # TODO: get the title, overview, and poster_path from the movie
    # dictionary. Then, get the release_date and convert it to a
    # datetime object with datetime.strptime

   

# TODO: create a user here
for n in range(10): # n - number of user - user1, user2, user3 ......
    email = f'user{n}@test.com'  # Voila! A unique email!
    password = 'test'

    add_user = crud.create_user(email,password)

    # created the user, Now let us add rows in the ratings table for the user
    # TODO: create 10 ratings for the user
    for r in range(10): 

        random_movie = choice(movies_in_db)
        score = randint(1,5)

        crud.create_rating(add_user,random_movie,score)

   

    