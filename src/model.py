from flask_login import UserMixin
from sqlalchemy.sql import func
from markupsafe import Markup
from src import db


class User(UserMixin, db.Model):
    __tablename__ = "users"

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
                    
class RatingF(db.Model):
    __tablename__ = "ratingf"
    
    rating_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    fountain_id = db.Column(db.Integer, db.ForeignKey('restaurants.rest_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    star_rating = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(2000), nullable=True)
    
    def __repr__(self):
        return f"""<RatingF id={self.rating_id}
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


def total_ratings(rest_id):
    return Rating.query.filter_by(rest_id=rest_id).count()

def star_avg(rest_id, total_ratings):
    total_stars = Rating.query.with_entities(func.sum(Rating.star_rating).filter(Rating.rest_id==rest_id).label('total')).first().total
    return round((total_stars/total_ratings), 1)

def total_ratings_fountain(id):
    return Fountain.query.filter_by(id=id).count()    

def star_avg_fountain(id, total_ratings_fountain):
    total_stars = Fountain.query.with_entities(func.sum(RatingF.star_rating).filter(RatingF.fountain_id==id).label('total')).first().total
    return round((total_stars/total_ratings_fountain), 1)

def restaurant_reviews(rest_id):
    return Rating.query.filter_by(rest_id=rest_id).all()

def get_user(user_id):
    return User.query.get(user_id)

def get_restaurant(rest_id):
    return Restaurant.query.get(rest_id)

def get_star_rating(user_id, rest_id):
    return (Rating.query.filter_by(user_id=user_id, rest_id=rest_id).first()).star_rating

def generate_stars(stars):
    if stars > 4.8:
        return Markup("""
            <strong><i class="fas fa-star star"></i><i class="fas fa-star star"></i><i class="fas fa-star star"></i><i class="fas fa-star star"></i><i class="fas fa-star star"></i></strong>
            """)
    elif stars >= 4.4:
        return Markup("""
            <strong><i class="fas fa-star star"></i><i class="fas fa-star star"></i><i class="fas fa-star star"></i><i class="fas fa-star star"><i class="fa-solid fa-star-half-stroke"></i></i></strong>
            """)
    elif stars >= 4:
        return Markup("""
            <strong><i class="fas fa-star star"></i><i class="fas fa-star star"></i><i class="fas fa-star star"></i><i class="fas fa-star star"></i><i class="fa-regular fa-star"></i></strong>
            """)
    elif stars >= 3.5:
        return Markup("""
            <strong><i class="fas fa-star star"></i><i class="fas fa-star star"></i><i class="fas fa-star star"></i><i class="fa-solid fa-star-half-stroke"></i></i><i class="fa-regular fa-star"></i></strong>
            """)
    elif stars >= 3:
        return Markup("""
            <strong><i class="fas fa-star star"></i><i class="fas fa-star star"></i><i class="fas fa-star star"></i><i class="fa-regular fa-star"></i><i class="fa-regular fa-star"></i></strong>
            """)
    elif stars >= 2.5:
        return Markup("""
            <strong><i class="fas fa-star star"></i><i class="fas fa-star star"></i><i class="fa-solid fa-star-half-stroke"></i></i><i class="fa-regular fa-star"></i><i class="fa-regular fa-star"></i></strong>
            """)
    elif stars >= 2:
        return Markup("""
            <strong><i class="fas fa-star star"></i><i class="fas fa-star star"></i><i class="fa-regular fa-star"></i><i class="fa-regular fa-star"></i><i class="fa-regular fa-star"></i></strong>
            """)
    elif stars >= 1.5:
        return Markup("""
            <strong><i class="fas fa-star star"></i><i class="fa-solid fa-star-half-stroke"><i class="fa-regular fa-star"></i><i class="fa-regular fa-star"></i><i class="fa-regular fa-star"></i></i>
            """)
    else:
        return Markup("""
            <strong><i class="fas fa-star star"></i><i class="fa-regular fa-star"></i><i class="fa-regular fa-star"></i><i class="fa-regular fa-star"></i><i class="fa-regular fa-star"></i></strong>
            """)

# def connect_to_db(app):
#     app.config['SQLALCHEMY_DATABASE_URI'] = environ["POSTGRES_URI"]
#     app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#     db.app = app
#     db.init_app(app)


# if __name__ == "__main__":
#     # As a convenience, if we run this module interactively, it will leave
#     # you in a state of being able to work with the database directly.
#     from main import app
#     connect_to_db(app)
#     print("Connected to DB.")
