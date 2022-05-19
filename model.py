from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from sqlalchemy.sql import func


db = SQLAlchemy()


class User(UserMixin, db.Model):
    __tablename__ = "users"
    # if tablename not set, automatically creates lower case version 
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(250), nullable=False)
    password = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), nullable=True)
    age = db.Column(db.Integer, nullable=True)
    zipcode = db.Column(db.String(250), nullable=True)
    
    def __repr__(self):
        return f"<User id={self.id} username={self.username}>"


class Restaurant(db.Model):
    __tablename__ = "restaurants"
    
    rest_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    land = db.Column(db.String(250), nullable=True)
    expense = db.Column(db.String, nullable=True)
    image_url = db.Column(db.String(500), nullable=True)
    description = db.Column(db.String(2000), nullable=True)
    full_service = db.Column(db.Boolean, nullable=True)
    breakfast = db.Column(db.Boolean, nullable=True)
    american = db.Column(db.Boolean, nullable=True)
    southern = db.Column(db.Boolean, nullable=True)
    mexican = db.Column(db.Boolean, nullable=True)
    italian = db.Column(db.Boolean, nullable=True)
    dessert = db.Column(db.Boolean, nullable=True)
    snacks = db.Column(db.Boolean, nullable=True)
    coffee = db.Column(db.Boolean, nullable=True)
    beverage_only = db.Column(db.Boolean, nullable=True)
    x_coord = db.Column(db.Numeric, nullable=True)
    y_coord = db.Column(db.Numeric, nullable=True)
    
    def __repr__(self):
        return f"""<Restaurant rest_id={self.rest_id} 
                    name={self.name}>
                    """
    
class Rating(db.Model):
    __tablename__ = "ratings"
    
    rating_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    rest_id = db.Column(db.Integer, db.ForeignKey('restaurants.rest_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    star_rating = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(2000), nullable=True)
    
    def __repr__(self):
        return f"""<Rating rating_id={self.rating_id}
                    rest_id={self.rest_id}
                    user_id={self.user_id}
                    star_rating={self.star_rating}>
                    """



def total_ratings(rest_id):
        return Rating.query.filter_by(rest_id=rest_id).count()
    
def star_avg(rest_id, total_ratings):
    total_stars = Rating.query.with_entities(func.sum(Rating.star_rating).filter(Rating.rest_id==rest_id).label('total')).first().total
    return round((total_stars/total_ratings), 1)


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
