from eating import db
from eating.model import (
    User,
    Restaurant,
    RestaurantCuisine,
    Rating,
    Fountain,
    FountainRating,
    Cuisine,
)
from werkzeug.security import generate_password_hash
from sqlalchemy.sql import func
from markupsafe import Markup
import random

"""
Users
"""


def get_all_users():
    return User.query.all()


def get_user_by_id(user_id):
    return User.query.filter_by(id=user_id).first()


def get_user_by_username(username):
    return User.query.filter_by(username=username).first()


def create_user(username, password, email, age, zipcode):
    new_user = User(
        username=username, password=password, email=email, age=age, zipcode=zipcode
    )
    db.session.add(new_user)
    db.session.commit()
    db.session.close()
    return new_user


def delete_user(user):
    db.session.delete(user)
    db.session.commit()
    db.session.close()
    return "User deleted"


"""
Restaurants
"""


def get_all_restaurants():
    return Restaurant.query.all()


def get_3_restaurants():
    return random.sample(Restaurant.query.all(), k=3)


def get_restaurant_by_id(rest_id):
    return Restaurant.query.filter_by(rest_id=rest_id).first()


def get_restaurant_by_name(name):
    return Restaurant.query.filter_by(name=name).first()


def total_ratings(rest_id):
    return Rating.query.filter_by(rest_id=rest_id).count()


def star_avg(rest_id, total_ratings):
    total_stars = (
        Rating.query.with_entities(
            func.sum(Rating.star_rating)
            .filter(Rating.rest_id == rest_id)
            .label("total")
        )
        .first()
        .total
    )

    try:
        return round((total_stars / total_ratings), 1)
    except:
        return 0


def restaurant_reviews(rest_id):
    return Rating.query.filter_by(rest_id=rest_id).all()


def get_star_rating(user_id, rest_id):
    return (
        Rating.query.filter_by(user_id=user_id, rest_id=rest_id).first()
    ).star_rating


def restaurants_count():
    return Restaurant.query.count()


def create_restaurant(name, image_url, land, expense, full_service, x_coord, y_coord):
    new_restaurant = Restaurant(
        name=name,
        image_url=image_url,
        land=land,
        expense=expense,
        full_service=full_service,
        x_coord=x_coord,
        y_coord=y_coord,
    )
    db.session.add(new_restaurant)
    db.session.commit()
    db.session.close()

    return new_restaurant


def update_restaurant(
    rest_id, name, image_url, land, expense, full_service, x_coord, y_coord
):
    restaurant = Restaurant.query.get(rest_id)
    restaurant.name = name if name else restaurant.name
    restaurant.image_url = image_url if image_url else restaurant.image_url
    restaurant.land = land if land else restaurant.land
    restaurant.expense = expense if expense else restaurant.expense
    restaurant.full_service = full_service if full_service else restaurant.full_service
    restaurant.x_coord = x_coord if x_coord else restaurant.x_coord
    restaurant.y_coord = y_coord if y_coord else restaurant.y_coord

    db.session.commit()
    db.session.close()

    return restaurant


"""
Cuisines
"""


def get_all_cuisines():
    return Cuisine.query.all()


def get_cuisine_by_name(name):
    return Cuisine.query.filter_by(name=name).first()


"""
Fountains
"""


def get_all_fountains():
    return Fountain.query.all()


def get_fountain_by_id(fountain_id):
    return Fountain.query.filter_by(id=fountain_id).first()


def get_fountain_by_name(name):
    return Fountain.query.filter_by(name=name).first()


def total_ratings_fountain(id):
    return Fountain.query.filter_by(id=id).count()


def star_avg_fountain(id, total_ratings_fountain):
    total_stars = (
        Fountain.query.with_entities(
            func.sum(FountainRating.star_rating)
            .filter(FountainRating.fountain_id == id)
            .label("total")
        )
        .first()
        .total
    )
    try:
        return round((total_stars / total_ratings_fountain), 1)
    except:
        return 0


def create_fountain(name, image_url, land, description, x_coord, y_coord):
    new_fountain = Fountain(
        name=name,
        image_url=image_url,
        land=land,
        description=description,
        x_coord=x_coord,
        y_coord=y_coord,
    )
    db.session.add(new_fountain)
    db.session.commit()
    db.session.close()

    return new_fountain


"""
Restaurant Ratings
"""


def get_user_ratings(user_id):
    return Rating.query.filter_by(user_id=user_id).all()


def get_user_restaurant_rating(user_id, rest_id):
    return Rating.query.filter_by(user_id=user_id, rest_id=rest_id).first()


def create_rating(user_id, rest_id, star_rating, review):
    new_rating = Rating(
        user_id=user_id, rest_id=rest_id, star_rating=star_rating, review=review
    )
    db.session.add(new_rating)
    db.session.commit()
    db.session.close()

    return new_rating


def delete_user_restaurant_rating(rest_id):
    rating = Rating.query.get(rest_id)
    db.session.delete(rating)
    db.session.commit()
    db.session.close()


"""
Fountain Ratings
"""


def get_user_rating_for_fountain(user_id, fountain_id):
    return FountainRating.query.filter_by(
        user_id=user_id, fountain_id=fountain_id
    ).first()


def create_fountain_rating(user_id, fountain_id, star_rating, review):
    new_rating = FountainRating(
        user_id=user_id, fountain_id=fountain_id, star_rating=star_rating, review=review
    )
    db.session.add(new_rating)
    db.session.commit()
    db.session.close()

    return new_rating


"""
Other
"""


def generate_stars(stars):
    if stars > 4.8:
        return Markup(
            """
            <strong><i class="fas fa-star star"></i><i class="fas fa-star star"></i><i class="fas fa-star star"></i><i class="fas fa-star star"></i><i class="fas fa-star star"></i></strong>
            """
        )
    elif stars >= 4.4:
        return Markup(
            """
            <strong><i class="fas fa-star star"></i><i class="fas fa-star star"></i><i class="fas fa-star star"></i><i class="fas fa-star star"><i class="fa-solid fa-star-half-stroke"></i></i></strong>
            """
        )
    elif stars >= 4:
        return Markup(
            """
            <strong><i class="fas fa-star star"></i><i class="fas fa-star star"></i><i class="fas fa-star star"></i><i class="fas fa-star star"></i><i class="fa-regular fa-star"></i></strong>
            """
        )
    elif stars >= 3.5:
        return Markup(
            """
            <strong><i class="fas fa-star star"></i><i class="fas fa-star star"></i><i class="fas fa-star star"></i><i class="fa-solid fa-star-half-stroke"></i></i><i class="fa-regular fa-star"></i></strong>
            """
        )
    elif stars >= 3:
        return Markup(
            """
            <strong><i class="fas fa-star star"></i><i class="fas fa-star star"></i><i class="fas fa-star star"></i><i class="fa-regular fa-star"></i><i class="fa-regular fa-star"></i></strong>
            """
        )
    elif stars >= 2.5:
        return Markup(
            """
            <strong><i class="fas fa-star star"></i><i class="fas fa-star star"></i><i class="fa-solid fa-star-half-stroke"></i></i><i class="fa-regular fa-star"></i><i class="fa-regular fa-star"></i></strong>
            """
        )
    elif stars >= 2:
        return Markup(
            """
            <strong><i class="fas fa-star star"></i><i class="fas fa-star star"></i><i class="fa-regular fa-star"></i><i class="fa-regular fa-star"></i><i class="fa-regular fa-star"></i></strong>
            """
        )
    elif stars >= 1.5:
        return Markup(
            """
            <strong><i class="fas fa-star star"></i><i class="fa-solid fa-star-half-stroke"><i class="fa-regular fa-star"></i><i class="fa-regular fa-star"></i><i class="fa-regular fa-star"></i></i>
            """
        )
    elif stars >= 1:
        return Markup(
            """
            <strong><i class="fas fa-star star"></i><i class="fa-regular fa-star"></i><i class="fa-regular fa-star"></i><i class="fa-regular fa-star"></i><i class="fa-regular fa-star"></i></strong>
            """
        )
    elif stars >= 0.2:
        return Markup(
            """
            <strong><i class="fa-solid fa-star-half-stroke"></i><i class="fa-regular fa-star"></i><i class="fa-regular fa-star"></i><i class="fa-regular fa-star"></i><i class="fa-regular fa-star"></i></strong>
            """
        )
    else:
        return Markup(
            """
            <strong></i><i class="fa-regular fa-star"></i><i class="fa-regular fa-star"></i><i class="fa-regular fa-star"></i><i class="fa-regular fa-star"></i><i class="fa-regular fa-star"></i></strong>
            """
        )
