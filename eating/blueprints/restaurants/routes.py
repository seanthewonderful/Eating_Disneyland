from flask import Blueprint, render_template, redirect, flash, url_for
import eating.crud as crud
from eating.forms import AddRestaurant, RateRestaurant
from flask_login import current_user

"""Restaurant Blueprint"""

restaurants_bp = Blueprint("restaurants_bp", "__name__")


""" Restaurant Routes """


@restaurants_bp.route("/restaurants")
def restaurants():
    """Renders page with all restaurants from db"""

    restaurants = crud.get_all_restaurants()

    return render_template(
        "restaurants.html",
        restaurants=restaurants,
        total_ratings=crud.total_ratings,
        star_avg=crud.star_avg,
        generate_stars=crud.generate_stars,
    )


@restaurants_bp.route("/add_restaurant", methods=["GET", "POST"])
def add_restaurant():
    """Return page to add a new restaurant, accepts and processes new restaurant submission"""

    form = AddRestaurant()

    if form.validate_on_submit():
        if crud.get_restaurant_by_name(name=form.name.data):
            # if Restaurant.query.filter_by(name=form.name.data).first():
            flash("Restaurant already exists", category="danger")
            return redirect(url_for("restaurants_bp.add_restaurant"))

        # cuisines = []
        # for cuisine in form.cuisines.data:
        #     cuisines.append(get_cuisine_by_name(cuisine))

        # print(cuisines)

        crud.create_restaurant(
            name=form.name.data,
            image_url=form.image_url.data,
            land=form.land.data,
            expense=form.expense.data,
            full_service=form.full_service.data,
            x_coord=form.x_coord.data,
            y_coord=form.y_coord.data,
        )

        flash("Restaurant added successfully", category="success")

        return redirect(url_for("restaurants_bp.add_restaurant"))

    return render_template("addrestaurant.html", form=form)


@restaurants_bp.route("/eating_place/<rest_id>", methods=["GET", "POST"])
def eating_place(rest_id):
    """Renders page for specific restaurant, POST creates a new rating for the restaurant"""

    form = RateRestaurant()
    restaurant = crud.get_restaurant_by_id(rest_id)
    rest_len = crud.restaurants_count()

    if current_user.is_authenticated:
        user_id = current_user.id
        rated = crud.get_user_restaurant_rating(user_id=user_id, rest_id=rest_id)

        if form.validate_on_submit():
            star_rating = form.star_rating.data
            review = form.review.data

            # if Rating.query.filter_by(user_id=user_id, rest_id=rest_id).first():
            #     pass # what was I doing here?

            crud.create_rating(
                user_id=user_id, rest_id=rest_id, star_rating=star_rating, review=review
            )

            flash("Your review has been accepted, thank you!", category="success")

            return redirect(url_for("restaurants_bp.eating_place", rest_id=rest_id))

        return render_template(
            "eating_place.html",
            restaurant=restaurant,
            form=form,
            rated=rated,
            rest_len=rest_len,
            total_ratings=crud.total_ratings,
            star_avg=crud.star_avg,
            restaurant_reviews=crud.restaurant_reviews,
            get_user_by_id=crud.get_user_by_id,
            get_restaurant_by_id=crud.get_restaurant_by_id,
            generate_stars=crud.generate_stars,
            get_star_rating=crud.get_star_rating,
        )

    return render_template(
        "eating_place.html",
        restaurant=restaurant,
        form=form,
        rest_len=rest_len,
        total_ratings=crud.total_ratings,
        star_avg=crud.star_avg,
        restaurant_reviews=crud.restaurant_reviews,
        get_user_by_id=crud.get_user_by_id,
        get_restaurant_by_id=crud.get_restaurant_by_id,
        generate_stars=crud.generate_stars,
        get_star_rating=crud.get_star_rating,
    )


@restaurants_bp.route("/update_restaurant/<rest_id>", methods=["POST"])
def update_restaurant(rest_id):
    """Updates information about a restaurant"""

    pass
