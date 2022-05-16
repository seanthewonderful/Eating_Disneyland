import model
from flask_sqlalchemy import SQLAlchemy


rests = model.Restaurant.query.all()

if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    from main import app
    model.connect_to_db(app)
    print("Connected to DB.")


