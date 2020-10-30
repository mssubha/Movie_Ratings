""" CRUD operations"""

from model import db, User, Movie, Rating, connect_to_db
from datetime import datetime


def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)
    # user = User(email="test@test.test", password="123")

    db.session.add(user)
    db.session.commit()

    return user

# test_user = create_user("test@test.test","123")

def create_movie(title, overview, release_date, poster_path):
    """Create and return a new movie."""
    movie = Movie(title=title, overview=overview,
                  release_date=release_date, poster_path=poster_path)

    db.session.add(movie)
    db.session.commit()

    return movie

# create_movie("Supergirls", "About Subha and Elvira", '2020, 10, 02', "tests/ereer.t.gif")
# Make a not on the date format above

def create_rating(user,movie,score):
    # rating = Rating(score= score, movie_id = movie.movie_id, user_id = user.user_id)
    rating = Rating(user=user, movie=movie, score=score)

    db.session.add(rating)
    db.session.commit()

    return rating

if __name__ == '__main__':
    from server import app
    connect_to_db(app)