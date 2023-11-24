from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, login_user, logout_user, current_user
import eating.crud as crud
from eating import db
from eating.forms import UpdateUser
from werkzeug.security import generate_password_hash

users_bp = Blueprint("users_bp", "__name__")


@users_bp.route("/my_contributions", methods=["GET", "POST"])
@login_required
def my_contributions():
    """Renders user's contribution page. POST - submits update to a rating"""

    # reviews = Rating.query.filter_by(user_id=current_user.id).all()
    reviews = crud.get_user_ratings(current_user.id)
    restaurants = crud.get_all_restaurants()

    if request.method == "POST":
        try:
            print(request.form["rating_"])

        except:
            rest_id = request.form["rest_id"]
            # rating = Rating.query.filter_by(
            #     user_id=current_user.id, rest_id=rest_id
            # ).first()
            rating = crud.get_user_restaurant_rating(
                user_id=current_user.id, rest_id=rest_id
            )
            rating.star_rating = request.form["star_rating"]
            rating.review = request.form["review"]
            db.session.commit()
            db.session.close()
            flash("Updates made.", category="success")
            return redirect(url_for("users_bp.my_contributions"))

        else:
            # rating = Rating.query.get(request.form["rating_"])
            # db.session.delete(rating)
            # db.session.commit()
            # db.session.close()
            crud.delete_user_restaurant_rating(rest_id=request.form["rating_"])
            flash("Rating deleted. It's as if you never ate there.", category="danger")
            return redirect(url_for("users_bp.my_contributions"))

    return render_template(
        "my_contributions.html",
        reviews=reviews,
        restaurants=restaurants,
        get_restaurant_by_id=crud.get_restaurant_by_id,
        generate_stars=crud.generate_stars,
    )


@users_bp.route("/profile", methods=["GET", "POST"])
@login_required
def profile():
    """Renders user's profile page. POST - submits changes to user info"""

    form = UpdateUser()

    if form.validate_on_submit():
        username = (form.username.data).lower()
        password = generate_password_hash(
            form.password.data, method="pbkdf2:sha256", salt_length=8
        )
        email = form.email.data
        age = form.age.data
        zipcode = form.zipcode.data

        if crud.get_user_by_username(username=username):
            flash(
                "That's such a great Username that it's already been taken! So sorry, please try a different Username.",
                category="warning",
            )
            return redirect(url_for("users_bp.profile"))

        current_user.username = username
        current_user.password = password
        current_user.email = email
        current_user.age = age
        current_user.zipcode = zipcode
        db.session.commit()
        db.session.close()
        flash("Updates made.", category="success")

        return redirect(url_for("users_bp.profile"))

    return render_template("profile.html", form=form)
