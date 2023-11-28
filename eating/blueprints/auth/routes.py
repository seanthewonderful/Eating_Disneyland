from flask import Blueprint, render_template, redirect, url_for, flash
import eating.crud as crud
from flask_login import (
    login_manager,
    login_required,
    current_user,
    login_user,
    logout_user,
)
from eating.forms import LoginForm, RegisterForm, DeleteUser
from werkzeug.security import check_password_hash, generate_password_hash


auth_bp = Blueprint("auth_bp", "__name__")


""" Login/Logout/Register Routes """


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    """Renders login page, POST logs in a user"""

    form = LoginForm()

    if form.validate_on_submit():
        user = crud.get_user_by_username(username=(form.username.data).lower())

        if user:
            password = form.password.data

            if check_password_hash(user.password, password):
                login_user(user)
                flash("Flight to LoginLand successful", category="success")
                return redirect(url_for("main.home"))

            else:
                flash("Incorrect password", category="danger")
                return redirect(url_for("auth_bp.login"))

        else:
            flash(
                "No such username exists...yet. Please register to claim it!",
                category="warning",
            )
            return redirect(url_for("auth_bp.login"))

    return render_template("login.html", form=form)


@auth_bp.route("/logout")
def logout():
    """Logs a user out"""

    logout_user()
    flash("Now leaving LoginLand. Please fly our way again!", category="primary")

    return redirect(url_for("main.home"))


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    """Renders user registration page. POST - registers a user"""

    form = RegisterForm()

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
                "That's such a great Username that it's already been taken! So sorry, please try a different name.",
                category="warning",
            )
            return redirect(url_for("auth_bp.register"))

        # new_user = User(
        #     username=username, password=password, email=email, age=age, zipcode=zipcode
        # )
        # db.session.add(new_user)
        # db.session.commit()
        new_user = crud.create_user(
            username=username, password=password, email=email, age=age, zipcode=zipcode
        )

        flash(
            "Account created! Please login with your credentials.", category="success"
        )

        # db.session.close()

        return redirect(url_for("auth_bp.login"))

    return render_template("register.html", form=form)


@auth_bp.route("/delete_user", methods=["GET", "POST"])
@login_required
def delete_user():
    """Page to delete a user from the db, accepts post to delete user"""

    form = DeleteUser()

    if form.validate_on_submit():
        print("form validated")
        crud.delete_user(user=current_user)
        # db.session.delete(current_user)
        # db.session.commit()
        # db.session.close()
        flash(
            "Account sent to the Memory Dump. Now perusing as a guest!", category="info"
        )
        return redirect(url_for("main.home"))

    return render_template("delete_user.html", form=form)
