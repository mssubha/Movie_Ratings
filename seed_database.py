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

with open('data/movies.json') as f:
    movie_data = json.loads(f.read())