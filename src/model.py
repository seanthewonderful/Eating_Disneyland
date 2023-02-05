from flask_login import UserMixin
from sqlalchemy.sql import func
from markupsafe import Markup
from src.server import db
import os


class User(UserMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(250), nullable=False)
    password = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), nullable=True)
    age = db.Column(db.Integer, nullable=True)
    zipcode = db.Column(db.String(250), nullable=True)
    
    ratings = db.Relationship("Rating", back_populates="user")
    
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
    # breakfast = db.Column(db.Boolean, nullable=True)
    # american = db.Column(db.Boolean, nullable=True)
    # southern = db.Column(db.Boolean, nullable=True)
    # mexican = db.Column(db.Boolean, nullable=True)
    # italian = db.Column(db.Boolean, nullable=True)
    # dessert = db.Column(db.Boolean, nullable=True)
    # snacks = db.Column(db.Boolean, nullable=True)
    # coffee = db.Column(db.Boolean, nullable=True)
    # beverage_only = db.Column(db.Boolean, nullable=True)
    x_coord = db.Column(db.Numeric, nullable=True)
    y_coord = db.Column(db.Numeric, nullable=True)
    
    ratings = db.relationship("Rating", back_populates="restaurant")
    cuisines = db.relationship("Cuisine", back_populates="restaurant")
    
    def __repr__(self):
        return f"""<Restaurant rest_id={self.rest_id} 
                    name={self.name}>
                    """

class Cuisine(db.Model):
    __tablename__ = "cuisines"
    
    cuisine_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(30), unique=True)
    
    restaurant = db.relationship("Restaurant", back_populates="cuisines")
    
    def __repr__(self):
        return f"""<Cuisine: {self.name} 
                    cuisine_id: {self.cuisine_id}>"""
    
class RestaurantCuisine(db.Model):
    """Junction table to associate restaurants with cuisines"""
    
    __tablename__ = "restaurant_cuisines"
    
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    rest_id = db.Column(db.Integer, db.ForeignKey("restaurants.rest_id"))
    cuisine_id = db.Column(db.Integer, db.ForeignKey("cuisines.cuisine_id"))
    
    # def __repr__(self):
    #     return f"""<RestaurantCuisine id: {self.id}
    #                 restaurant: {self.rest_id}
    #                 cuisine_id: {self.cuisine_id}>"""

class Rating(db.Model):
    __tablename__ = "ratings"
    
    rating_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    rest_id = db.Column(db.Integer, db.ForeignKey('restaurants.rest_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    star_rating = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(2000), nullable=True)
    
    restaurant = db.Relationship("Restaurant", back_populates="ratings")
    user = db.Relationship("User", back_populates="ratings")
    
    def __repr__(self):
        return f"""<Rating rating_id={self.rating_id}
                    rest_id={self.rest_id}
                    user_id={self.user_id}
                    star_rating={self.star_rating}>
                    """
                    
class FountainRating(db.Model):
    __tablename__ = "fountain_ratings"
    
    rating_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    fountain_id = db.Column(db.Integer, db.ForeignKey('restaurants.rest_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    star_rating = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(2000), nullable=True)
    
    def __repr__(self):
        return f"""<Fountain Rating: id={self.rating_id}
                    fountain_id={self.fountain_id}
                    user_id={self.user_id}
                    star_rating={self.star_rating}>
                    """

class Fountain(db.Model):
    __tablename__ = "fountains"
    
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    land = db.Column(db.String(250), nullable=True)
    image_url = db.Column(db.String(500), nullable=True)
    description = db.Column(db.String(2000), nullable=True)
    x_coord = db.Column(db.Numeric, nullable=True)
    y_coord = db.Column(db.Numeric, nullable=True)
    
    def __repr__(self):
        return f"""<Fountain id={self.id} 
                    name={self.name}>
                    """



def connect_to_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ["POSTGRES_URI"]
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.
    from server import app
    connect_to_db(app)
    print("Connected to DB.")
