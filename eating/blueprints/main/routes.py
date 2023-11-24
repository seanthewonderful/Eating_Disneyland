from flask import Blueprint, render_template
import eating.crud as crud

main = Blueprint("main", "__name__")


@main.route("/")
def home():
    """Homepage"""

    restaurants = crud.get_3_restaurants()

    return render_template(
        "home.html",
        restaurants=restaurants,
        total_ratings=crud.total_ratings,
        star_avg=crud.star_avg,
        generate_stars=crud.generate_stars,
    )
