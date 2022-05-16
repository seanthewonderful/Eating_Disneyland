import model
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()



def connect_to_db(app):
    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///disneyland_ratings'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)



if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    from main import app
    connect_to_db(app)
    print("Connected to DB.")

    pizza = model.Restaurant.query.filter_by(name='Alien Pizza Planet').first()

    print(pizza)