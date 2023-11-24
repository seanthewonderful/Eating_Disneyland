from dataclasses import dataclass
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
import os
from eating import db, login_manager


"""Flask login_manager functions"""


@login_manager.user_loader
def load_user(user_id):
    """LoginManager's user_loader"""

    return User.query.get(int(user_id))


# @login_manager.user_loader
# def load_admin(admin_id):
#     """LoginManager's admin loader"""
#     return Admin.query.get(int(admin_id))


@login_manager.unauthorized_handler
def unauthorized():
    """Deny unauthorized users"""

    return "Please login to view this page"


"""Models"""


class User(UserMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)

    username = db.Column(db.String(250), nullable=False)
    password = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), nullable=True)
    age = db.Column(db.Integer, nullable=True)
    zipcode = db.Column(db.String(250), nullable=True)

    restaurant_ratings = db.relationship("Rating", back_populates="user")
    fountain_ratings = db.relationship("FountainRating", back_populates="user")

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
    x_coord = db.Column(db.Numeric, nullable=True)
    y_coord = db.Column(db.Numeric, nullable=True)

    ratings = db.relationship("Rating", back_populates="restaurant")
    cuisines = db.relationship("RestaurantCuisine", back_populates="restaurant")

    def __repr__(self):
        return f"<Restaurant rest_id={self.rest_id} name={self.name}>"


class Cuisine(db.Model):
    __tablename__ = "cuisines"

    cuisine_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(30), unique=True)

    restaurants = db.relationship("RestaurantCuisine", back_populates="cuisine")

    def __repr__(self):
        return f"<Cuisine: {self.name} cuisine_id: {self.cuisine_id}>"


class RestaurantCuisine(db.Model):
    """Junction table to associate restaurants with cuisines"""

    __tablename__ = "restaurant_cuisines"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    restaurant = db.relationship("Restaurant", back_populates="cuisines")
    cuisine = db.relationship("Cuisine", back_populates="restaurants")

    rest_id = db.Column(db.Integer, db.ForeignKey("restaurants.rest_id"))
    cuisine_id = db.Column(db.Integer, db.ForeignKey("cuisines.cuisine_id"))

    def __repr__(self):
        return f"<RestaurantCuisine id: {self.id} restaurant: {self.restaurant} cuisine_id: {self.cuisine}>"


class Rating(db.Model):
    __tablename__ = "ratings"

    rating_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    star_rating = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(2000), nullable=True)

    restaurant = db.relationship("Restaurant", back_populates="ratings")
    user = db.relationship("User", back_populates="restaurant_ratings")

    rest_id = db.Column(db.Integer, db.ForeignKey("restaurants.rest_id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def __repr__(self):
        return f"<Rating rating_id={self.rating_id} restaurant={self.restaurant} user={self.user} star_rating={self.star_rating} review={self.review}>"


class FountainRating(db.Model):
    __tablename__ = "fountain_ratings"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    star_rating = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(2000), nullable=True)

    fountain = db.relationship("Fountain", back_populates="ratings")
    user = db.relationship("User", back_populates="fountain_ratings")

    fountain_id = db.Column(db.Integer, db.ForeignKey("fountains.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def __repr__(self):
        return f"<Fountain Rating: id={self.id} fountain_id={self.fountain_id} user_id={self.user_id} star_rating={self.star_rating}>"


class Fountain(db.Model):
    __tablename__ = "fountains"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    land = db.Column(db.String(250), nullable=True)
    image_url = db.Column(db.String(500), nullable=True)
    description = db.Column(db.String(2000), nullable=True)
    x_coord = db.Column(db.Numeric, nullable=True)
    y_coord = db.Column(db.Numeric, nullable=True)

    ratings = db.relationship("FountainRating", back_populates="fountain")

    def __repr__(self):
        return f"<Fountain id={self.id} name={self.name}>"


def connect_to_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["POSTGRES_URI"]
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SQLALCHEMY_ECHO"] = True
    app.config["FLASK_DEBUG"] = True

    db.app = app
    db.init_app(app)
    print("Connected to DB")


if __name__ == "__main__":
    from flask import current_app

    connect_to_db(current_app)
