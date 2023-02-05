from model import User, Restaurant, Rating, Fountain, FountainRating, Cuisine, RestaurantCuisine
from sqlalchemy.sql import func
from markupsafe import Markup

"""Users"""

def get_all_users():
    return User.query.all()

def get_user_by_id(user_id):
    return User.query.get(user_id)

def get_user_by_username(username):
    return User.query.filter_by(username=username).first()

"""Restaurants"""

def get_all_restaurants():
    return Restaurant.query.all()

def get_restaurant_by_id(rest_id):
    return Restaurant.query.get(rest_id)

def total_ratings(rest_id):
    return Rating.query.filter_by(rest_id=rest_id).count()

def star_avg(rest_id, total_ratings):
    total_stars = Rating.query.with_entities(func.sum(Rating.star_rating).filter(Rating.rest_id==rest_id).label('total')).first().total
    return round((total_stars/total_ratings), 1)

def restaurant_reviews(rest_id):
    return Rating.query.filter_by(rest_id=rest_id).all()

def get_star_rating(user_id, rest_id):
    return (Rating.query.filter_by(user_id=user_id, rest_id=rest_id).first()).star_rating

"""Cuisines"""

def get_all_cuisines():
    return Cuisine.query.all()

def get_cuisine_by_name(name):
    return Cuisine.query.filter_by(name=name).first()

"""Fountains"""

def get_all_fountains():
    return Fountain.query.all()

def get_fountain_by_id(fountain_id):
    return Fountain.query.get(fountain_id)

def total_ratings_fountain(id):
    return Fountain.query.filter_by(id=id).count()    

def star_avg_fountain(id, total_ratings_fountain):
    total_stars = Fountain.query.with_entities(func.sum(FountainRating.star_rating).filter(FountainRating.fountain_id==id).label('total')).first().total
    return round((total_stars/total_ratings_fountain), 1)

"""Other"""

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
        
        

if __name__ == "__main__":
    from server import app
    from model import connect_to_db
    
    connect_to_db(app)