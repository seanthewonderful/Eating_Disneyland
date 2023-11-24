from flask import Blueprint, render_template, redirect, flash, url_for
from flask_login import current_user
from eating.forms import RateFountain, AddFountain
import eating.crud as crud


"""Fountains Blueprint"""

fountains_bp = Blueprint("fountains_bp", "__name__")


""" Fountain Routes """


@fountains_bp.route("/fountain_place/<fountain_id>", methods=["GET", "POST"])
def fountain_place(fountain_id):
    """Renders page for specific fountain, POST creates a new rating for the fountain"""

    form = RateFountain()
    fountain = crud.get_fountain_by_id(fountain_id)

    if current_user.is_authenticated:
        user_id = current_user.id
        rated = crud.get_user_rating_for_fountain(
            user_id=user_id, fountain_id=fountain_id
        )

        if form.validate_on_submit():
            star_rating = form.star_rating.data
            review = form.review.data

            if rated:
                pass

            new_rating = crud.create_fountain_rating(
                user_id=user_id,
                fountain_id=fountain_id,
                star_rating=star_rating,
                review=review,
            )

            flash("Your review has been accepted, thank you!", category="success")
            return redirect(url_for("fountain_place", fountain_id=fountain_id))

        return render_template(
            "fountain_place.html", form=form, fountain=fountain, rated=rated
        )

    return render_template(
        "fountain_place.html", form=form, fountain=fountain, rated=rated
    )


@fountains_bp.route("/add_fountain", methods=["GET", "POST"])
def add_fountain():
    """Return page to add a new fountain, accepts and processes new fountain submission"""

    form = AddFountain()

    if form.validate_on_submit():
        if crud.get_fountain_by_name(name=form.name.data):
            flash("Fountain name already exists", category="danger")
            return redirect(url_for("add_fountain"))

        new_fountain = crud.create_fountain(
            name=form.name.data,
            image_url=form.image_url.data,
            land=form.land.data,
            description=form.description.data,
            x_coord=form.x_coord.data,
            y_coord=form.y_coord.data,
        )
        flash("Fountain added successfully", category="success")

        return redirect(url_for("add_fountain"))

    return render_template("add_fountain.html", form=form)
