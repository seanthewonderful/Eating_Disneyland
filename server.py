from flask import (Flask, redirect, render_template, 
                   flash, url_for, request)
from flask_login import (LoginManager, login_user, logout_user, login_required, current_user)
from flask_debugtoolbar import DebugToolbarExtension
from flask_wtf.csrf import CSRFProtect
from jinja2 import StrictUndefined
import random
from forms import (DeleteUser, UpdateUser, RegisterForm, LoginForm, 
                   AddRestaurant, RateRestaurant, AddFountain, RateFountain)
from model import (User, Restaurant, Fountain, Rating, FountainRating, db)
from crud import (total_ratings, star_avg, restaurant_reviews, get_user_by_id,
                  get_restaurant_by_id, generate_stars, get_star_rating, get_all_fountains,
                  get_all_restaurants, get_cuisine_by_name, get_user_by_username, get_fountain_by_id)
from make_map import (make_map, make_fountain_map)
from werkzeug.security import (generate_password_hash, check_password_hash)
from os import environ


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ["POSTGRES_URI"]
app.secret_key = environ["SECRET_KEY"]
csrf = CSRFProtect(app)
app.jinja_env.undefined = StrictUndefined
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"]=False
login_manager = LoginManager()
login_manager.init_app(app)


""" Home and Map Routes """

@app.route("/")
def home():
    """Show homepage"""
    
    restaurants = random.sample(Restaurant.query.all(), k=3)
    
    return render_template('home.html', restaurants=restaurants,
                           total_ratings=total_ratings, 
                           star_avg=star_avg,
                           generate_stars=generate_stars)

@app.route('/map')
def map():
    """Return restaurant map html"""
    
    make_map(get_all_restaurants())
    
    return render_template('disneyland_map.html')

@app.route('/fountain_map')
def fountain_map():
    """Return fountain map html"""
    
    make_fountain_map(get_all_fountains())
    
    return render_template('fountain_map.html')

""" Restaurant Routes """

@app.route('/restaurants')
def restaurants():
    """Renders page with all restaurants from db"""
    
    restaurants = get_all_restaurants()
    
    return render_template('restaurants.html', 
                           restaurants=restaurants, 
                           total_ratings=total_ratings, 
                           star_avg=star_avg,
                           generate_stars=generate_stars)

@app.route('/add_restaurant', methods=["GET", "POST"])
def add_restaurant():
    """Return page to add a new restaurant, accepts and processes new restaurant submission"""
    
    form = AddRestaurant()
    
    if form.validate_on_submit():
        
        if Restaurant.query.filter_by(name=form.name.data).first():
            
            flash("Restaurant already exists", category='danger')
            return redirect(url_for('add_restaurant'))

        # cuisines = []
        # for cuisine in form.cuisines.data:
        #     cuisines.append(get_cuisine_by_name(cuisine))
            
        # print(cuisines)
        
        new_restaurant = Restaurant(
            name = form.name.data,
            image_url = form.image_url.data,
            land = form.land.data,
            expense = form.expense.data,
            full_service = form.full_service.data,
            x_coord = form.x_coord.data,
            y_coord = form.y_coord.data
            )
        
        db.session.add(new_restaurant)
        db.session.commit()
        flash("Restaurant added successfully", category='success')
        
        return redirect(url_for('add_restaurant'))
    
    return render_template('addrestaurant.html', form=form)

@app.route('/eating_place/<rest_id>', methods=["GET", "POST"])
def eating_place(rest_id):
    """Renders page for specific restaurant, POST creates a new rating for the restaurant"""
    
    form = RateRestaurant()
    restaurant = get_restaurant_by_id(rest_id)
    rest_len = Restaurant.query.count()
    
    if current_user.is_authenticated:
        user_id = current_user.id
        rated = Rating.query.filter_by(user_id=user_id, rest_id=rest_id).first()
        
        if form.validate_on_submit():
            star_rating = form.star_rating.data
            review = form.review.data
            
            # if Rating.query.filter_by(user_id=user_id, rest_id=rest_id).first():
            #     pass # what was I doing here? 
            
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
                               rest_len=rest_len,
                               total_ratings=total_ratings,
                               star_avg=star_avg,
                               restaurant_reviews=restaurant_reviews, 
                               get_user_by_id=get_user_by_id,
                               get_restaurant_by_id=get_restaurant_by_id,
                               generate_stars=generate_stars,
                               get_star_rating=get_star_rating)
        
    return render_template('eating_place.html', 
                           restaurant=restaurant, 
                           form=form, 
                           rest_len=rest_len,
                           total_ratings=total_ratings,
                           star_avg=star_avg,
                           restaurant_reviews=restaurant_reviews,
                           get_user_by_id=get_user_by_id,
                           get_restaurant_by_id=get_restaurant_by_id,
                           generate_stars=generate_stars,
                           get_star_rating=get_star_rating)

@app.route('/update_restaurant/<rest_id>', methods=["POST"])
def update_restaurant(rest_id):
    """Updates information about a restaurant"""
    
    
    
    pass

""" Fountain Routes """

@app.route('/fountain_place/<fountain_id>', methods=["GET", "POST"])
def fountain_place(fountain_id):
    """Renders page for specific fountain, POST creates a new rating for the fountain"""
    
    form = RateFountain()
    fountain = get_fountain_by_id(fountain_id)
    
    if current_user.is_authenticated:
        
        user_id = current_user.id
        rated = FountainRating.query.filter_by(user_id=user_id, fountain_id=fountain_id).first()
        
        if form.validate_on_submit():
            
            star_rating = form.star_rating.data
            review = form.review.data
            
            if FountainRating.query.filter_by(user_id=user_id, fountain_id=fountain_id).first():
                pass
            new_rating = FountainRating(user_id=user_id,
                                 fountain_id=fountain_id,
                                 star_rating=star_rating,
                                 review=review)
            db.session.add(new_rating)
            db.session.commit()
            db.session.close()
            flash("Your review has been accepted, thank you!", category='success')
            return redirect(url_for('fountain_place', fountain_id=fountain_id))
        
        return render_template('fountain_place.html', 
                                form=form,
                                fountain=fountain,
                                rated=rated)
        
    return render_template('fountain_place.html', 
                           form=form,
                           fountain=fountain,
                           rated=rated)


@app.route('/add_fountain', methods=["GET", "POST"])
def add_fountain():
    """Return page to add a new fountain, accepts and processes new fountain submission"""
    
    form = AddFountain()
    
    if form.validate_on_submit():
        
        if Fountain.query.filter_by(name=form.name.data).first():
            
            flash("Fountain name already exists", category='danger')
            return redirect(url_for('add_fountain'))
        
        new_fountain = Fountain(
            name = form.name.data,
            image_url = form.image_url.data,
            land = form.land.data,
            description = form.description.data,
            x_coord = form.x_coord.data,
            y_coord = form.y_coord.data
            )
        db.session.add(new_fountain)
        db.session.commit()
        db.session.close()
        flash("Fountain added successfully", category='success')
        
        return redirect(url_for('add_fountain'))
    
    return render_template('add_fountain.html', form=form)

""" User Routes """

@app.route('/my_contributions', methods=["GET", "POST"])
@login_required
def my_contributions():
    """Renders user's contribution page. POST - submits update to a rating"""
    
    reviews = Rating.query.filter_by(user_id=current_user.id).all()
    restaurants = get_all_restaurants()
    
    if request.method == "POST":
        
        try:
            print(request.form['rating_'])
            
        except:
            rest_id = request.form['rest_id']
            rating = Rating.query.filter_by(user_id=current_user.id, rest_id=rest_id).first()
            rating.star_rating = request.form['star_rating']
            rating.review = request.form['review']
            db.session.commit()
            db.session.close()
            flash("Updates made.", category='success')
            return redirect(url_for('my_contributions'))
        
        else:
            rating = Rating.query.get(request.form['rating_'])
            db.session.delete(rating)
            db.session.commit()
            db.session.close()
            flash("Rating deleted. It's as if you never ate there.", category='danger')
            return redirect(url_for('my_contributions'))
    
    return render_template('my_contributions.html',  
                           reviews=reviews,
                           restaurants=restaurants,
                           get_restaurant_by_id=get_restaurant_by_id,
                           generate_stars=generate_stars)

@app.route('/profile', methods=["GET", "POST"])
@login_required
def profile():
    """Renders user's profile page. POST - submits changes to user info"""
    
    form = UpdateUser()

    if form.validate_on_submit():
        
        username = (form.username.data).lower()
        password = generate_password_hash(form.password.data, method='pbkdf2:sha256', salt_length=8)
        email = form.email.data
        age = form.age.data
        zipcode = form.zipcode.data
        
        if get_user_by_username(username=username):
            
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

""" Login/Logout/Register Routes """

@app.route('/login', methods=["GET", "POST"])
def login():
    """Renders login page, POST logs in a user"""
    
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
    """Logs a user out"""
    
    logout_user()
    flash("Now leaving LoginLand. Please fly our way again!", category='primary')
    
    return redirect(url_for('home'))

@app.route('/register', methods=["GET", "POST"])
def register():
    """Renders user registration page. POST - registers a user"""
    
    form = RegisterForm()
    
    if form.validate_on_submit():
        
        username = (form.username.data).lower()
        password = generate_password_hash(form.password.data, method='pbkdf2:sha256', salt_length=8)
        email = form.email.data
        age = form.age.data
        zipcode = form.zipcode.data
        
        if get_user_by_username(username=username):
            
            flash("That's such a great Username that it's already been taken! So sorry, please try a different Username.", category='warning')
            return redirect(url_for('register'))
        
        new_user = User(username=username,
                        password=password,
                        email=email,
                        age=age,
                        zipcode=zipcode
                        )
        db.session.add(new_user)
        db.session.commit()
        flash("Account created! Please login with your credentials.", category='success')
        
        db.session.close()
        
        return redirect(url_for('login'))
    
    return render_template('register.html', form=form)

@app.route('/delete_user', methods=["GET", "POST"])
@login_required
def delete_user():
    """Page to delete a user from the db, accepts post to delete user"""
    
    form = DeleteUser()
    
    if form.validate_on_submit():
        
        print("form validated")
        db.session.delete(current_user)
        db.session.commit()
        db.session.close()
        flash("Account sent to the Memory Dump. Now perusing as a guest!", category='info')
        return redirect(url_for('home'))
    
    return render_template('delete_user.html', form=form)

""" Flask Managers """

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@login_manager.unauthorized_handler
def unauthorized():
    return "Sorry, you must be logged in to view this page"

"""Custom image preview route"""

@app.route('/hp_image_preview')
def hp_image_preview():
    return render_template('hp_image_preview.html')



if __name__ == "__main__":
    from model import connect_to_db
    import os
    # app.jinja_env.auto_reload = app.debug
    # DebugToolbarExtension(app)
    os.system("source config.sh")
    connect_to_db(app)
    app.run()