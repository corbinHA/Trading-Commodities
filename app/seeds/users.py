from werkzeug.security import generate_password_hash
from app.models import db, User, Watchlist

# Adds a demo user, you can add other users here if you want


def seed_users():

    user = User(
        fullname='Mortimer Duke',
        username='TheDuke',
        email='mortimerduke@aa.io',
        password='password',
        balance=10000000.00
    )

    user.watchlist = Watchlist()

    db.session.add(user)
    db.session.commit()

# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and resets
# the auto incrementing primary key


def undo_users():
    db.session.execute('TRUNCATE users CASCADE;')
    db.session.commit()
