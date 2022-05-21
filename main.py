from flask import (Flask, redirect, render_template, 
                   flash, url_for, request)
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from flask_debugtoolbar import DebugToolbarExtension
from flask_wtf.csrf import CSRFProtect
from jinja2 import StrictUndefined
import random
from model import (connect_to_db, User, Restaurant, Rating, db, 
                   total_ratings, star_avg, restaurant_reviews, get_user, 
                   get_restaurant, generate_stars)
from forms import (DeleteUser, UpdateUser, RegisterForm, LoginForm, 
                   AddRestaurant, RateRestaurant)
from werkzeug.security import generate_password_hash, check_password_hash
from make_map import make_map


app = Flask(__name__)
app.secret_key = "6fb0ad050f264f45b1c29962f08ff548"
csrf = CSRFProtect(app)
app.jinja_env.undefined = StrictUndefined
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"]=False
login_manager = LoginManager()
login_manager.init_app(app)



""" Home and Map Routes """

@app.route("/")
def home():
    restaurants = random.choices(Restaurant.query.all(), k=3)
    return render_template('home.html', restaurants=restaurants,
                           total_ratings=total_ratings, 
                           star_avg=star_avg,
                           generate_stars=generate_stars)


@app.route('/map')
def map():
    restaurants = Restaurant.query.all()
    make_map(restaurants)
    return render_template('disneyland_map.html')

""" Alphabetical Page Routes"""


@app.route('/delete_user', methods=["GET", "POST"])
@login_required
def delete_user():
    form = DeleteUser()
    if form.validate_on_submit():
        print("form validated")
        db.session.delete(current_user)
        db.session.commit()
        db.session.close()
        flash("Account sent to the Memory Dump. Now perusing as a guest!", category='info')
        return redirect(url_for('home'))
    return render_template('delete_user.html', form=form)


@app.route('/eating_place/<rest_id>', methods=["GET", "POST"])
def eating_place(rest_id):
    form = RateRestaurant()
    restaurant = Restaurant.query.get(rest_id)
    previous_restaurant = Restaurant.query.get(int(rest_id) - 1)
    next_restaurant = Restaurant.query.get(int(rest_id) + 1)
    rest_len = Restaurant.query.count()
    if current_user.is_authenticated:
        user_id = current_user.id
        rated = Rating.query.filter_by(user_id=user_id, rest_id=rest_id).first()
        if form.validate_on_submit():
            star_rating = form.star_rating.data
            review = form.review.data
            if Rating.query.filter_by(user_id=user_id, rest_id=rest_id).first():
                pass
            new_rating = Rating(user_id=user_id,
                                rest_id=rest_id,
                                star_rating=star_rating,
                                review=review)
            db.session.add(new_rating)
            db.session.commit()
            db.session.close()
            flash("Your review has been accepted, thank you!", category='success')
            return redirect(url_for('eating_place', rest_id=rest_id))
        return render_template('eating_place.html', 
                               restaurant=restaurant, 
                               form=form, 
                               rated=rated, 
                               previous_restaurant=previous_restaurant, 
                               next_restaurant=next_restaurant,
                               rest_len=rest_len,
                               total_ratings=total_ratings,
                               star_avg=star_avg,
                               restaurant_reviews=restaurant_reviews, 
                               get_user=get_user,
                               generate_stars=generate_stars)
    return render_template('eating_place.html', 
                           restaurant=restaurant, 
                           form=form, 
                           previous_restaurant=previous_restaurant, 
                           next_restaurant=next_restaurant,
                           rest_len=rest_len,
                           total_ratings=total_ratings,
                           star_avg=star_avg,
                           restaurant_reviews=restaurant_reviews,
                           get_user=get_user,
                           generate_stars=generate_stars)



@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=(form.username.data).lower()).first()
        if user:
            password = form.password.data
            if check_password_hash(user.password, password):
                login_user(user)
                flash("Flight to LoginLand successful", category='success')
                return redirect(url_for('home'))
            else:
                flash("Incorrect password", category='danger')
                return redirect(url_for('login'))
        else:
            flash("No such username exists...yet. Please register to claim it!", category='warning')
            return redirect(url_for('login'))
    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    flash("Now leaving LoginLand. Please fly our way again!", category='primary')
    return redirect(url_for('home'))


@app.route('/my_contributions', methods=["GET", "POST"])
@login_required
def my_contributions():
    reviews = Rating.query.filter_by(user_id=current_user.id).all()
    restaurants = Restaurant.query.all()
    
    if request.method == "POST":
        rest_id = request.form['rest_id']
        rating = Rating.query.filter_by(user_id=current_user.id, rest_id=rest_id).first()
        rating.star_rating = request.form['star_rating']
        rating.review = request.form['review']
        db.session.commit()
        db.session.close()
        flash("Updates made.", category='success')
        return redirect(url_for('my_contributions'))
    
    return render_template('my_contributions.html',  
                           reviews=reviews,
                           restaurants=restaurants,
                           get_restaurant=get_restaurant,
                           generate_stars=generate_stars)


@app.route('/rating/delete', methods=["DELETE"])
@login_required
def delete_rating(user_id, rest_id):
    rating = Rating.query.filter_by(user_id=user_id, rest_id=rest_id).first()
    print(rating)


@app.route('/profile', methods=["GET", "POST"])
@login_required
def profile():
    form = UpdateUser()

    if form.validate_on_submit():
        username = (form.username.data).lower()
        password = generate_password_hash(form.password.data, method='pbkdf2:sha256', salt_length=8)
        email = form.email.data
        age = form.age.data
        zipcode = form.zipcode.data
        if User.query.filter_by(username=username).first():
            flash("That's such a great Username that it's already been taken! So sorry, please try a different Username.", category='warning')
            return redirect(url_for('profile'))
        
        current_user.username = username
        current_user.password = password
        current_user.email = email
        current_user.age = age
        current_user.zipcode = zipcode
        db.session.commit()
        db.session.close()
        flash("Updates made.", category='success')
        return redirect(url_for('profile'))
    
    return render_template('profile.html', form=form)


@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        username = (form.username.data).lower()
        password = generate_password_hash(form.password.data, method='pbkdf2:sha256', salt_length=8)
        email = form.email.data
        age = form.age.data
        zipcode = form.zipcode.data
        if User.query.filter_by(username=username).first():
            flash("That's such a great Username that it's already been taken! So sorry, please try a different Username.", category='warning')
            return redirect(url_for('register'))
        new_user = User(username=username,
                        password=password,
                        email=email,
                        age=age,
                        zipcode=zipcode)
        db.session.add(new_user)
        db.session.commit()
        db.session.close()
        flash("Account created! Please login with your credentials.", category='success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)


@app.route('/restaurants')
def restaurants():
    restaurants = Restaurant.query.all()
    return render_template('restaurants.html', 
                           restaurants=restaurants, 
                           total_ratings=total_ratings, 
                           star_avg=star_avg,
                           generate_stars=generate_stars)


@app.route('/add_restaurant', methods=["GET", "POST"])
def add_restaurant():
    form = AddRestaurant()
    if form.validate_on_submit():
        print("Form validated")
        if Restaurant.query.filter_by(name=form.name.data).first():
            flash("Restaurant already exists", category='danger')
            return redirect(url_for('add_restaurant'))
        new_restaurant = Restaurant(
            name = form.name.data,
            image_url = form.image_url.data,
            land = form.land.data,
            expense = form.expense.data,
            full_service = form.full_service.data,
            breakfast = form.breakfast.data,
            american = form.american.data,
            southern = form.southern.data,
            mexican = form.mexican.data,
            italian = form.italian.data,
            dessert = form.dessert.data,
            snacks = form.snacks.data,
            coffee = form.coffee.data,
            beverage_only = form.beverage_only.data
        )
        db.session.add(new_restaurant)
        db.session.commit()
        flash("Restaurant added successfully", category='success')
        return redirect(url_for('add_restaurant'))
    return render_template('addrestaurant.html', form=form)


""" Flask Managers """

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


if __name__ == "__main__":
    app.jinja_env.auto_reload = app.debug
    connect_to_db(app)
    DebugToolbarExtension(app)
    app.run(debug=True)