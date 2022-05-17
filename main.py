from flask import Flask, redirect, render_template, flash, url_for
from jinja2 import StrictUndefined
import folium
from flask_debugtoolbar import DebugToolbarExtension
# from flask_bootstrap import Bootstrap
# from map import Map
from model import connect_to_db, User, Restaurant, Rating, db
from forms import DeleteUser, UpdateUser, RegisterForm, LoginForm, AddRestaurant
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from make_map import make_map



app = Flask(__name__)
# Bootstrap(app)
app.secret_key = "6fb0ad050f264f45b1c29962f08ff548"

app.jinja_env.undefined = StrictUndefined
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"]=False
login_manager = LoginManager()
login_manager.init_app(app)


@app.route("/")
def home():
    return render_template('home.html')


@app.route('/map')
def map():
    restaurants = Restaurant.query.all()
    make_map(restaurants)
    return render_template('disneyland_map.html')


@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm()
    form.validate()
    if form.validate_on_submit():
        username = form.username.data
        password = generate_password_hash(form.password.data, method='pbkdf2:sha256', salt_length=8)
        email = form.email.data
        age = form.age.data
        zipcode = form.zipcode.data
        if User.query.filter_by(username=username).first():
            flash("That's such a great Username that it's already been taken! So sorry, please try a different Username.")
            return redirect(url_for('register'))
        new_user = User(username=username,
                        password=password,
                        email=email,
                        age=age,
                        zipcode=zipcode)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print("Validated")
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            print("User found")
            password = form.password.data
            if check_password_hash(user.password, password):
                print("PW Checked")
                login_user(user)
                flash("Flight to Loginland successful")
                return redirect(url_for('home'))
            else:
                flash("Incorrect password")
                return redirect(url_for('login'))
        else:
            flash("We find no records of that username, please register or type better")
            return redirect(url_for('login'))
    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    flash("Logged out.")
    return redirect(url_for('home'))


@app.route('/delete_user', methods=["GET", "POST"])
def delete_user():
    form = DeleteUser()
    # form.validate()
    if form.validate_on_submit():
        print("form validated")
        return redirect(url_for('delete_user'))
    return render_template('delete_user.html', form=form)


@app.route('/profile', methods=["GET", "POST"])
def profile():
    return render_template('profile.html')


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/restaurants')
def restaurants():
    restaurants = Restaurant.query.all()
    return render_template('restaurants.html', restaurants=restaurants)


@app.route('/add_restaurant', methods=["GET", "POST"])
def add_restaurant():
    form = AddRestaurant()
    if form.validate_on_submit():
        print("Form validated")
        if Restaurant.query.filter_by(name=form.name.data).first():
            flash("Restaurant already exists")
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
        flash("Restaurant added successfully")
        return redirect(url_for('add_restaurant'))
    return render_template('addrestaurant.html', form=form)


if __name__ == "__main__":
    app.jinja_env.auto_reload = app.debug
    connect_to_db(app)
    DebugToolbarExtension(app)
    app.run(debug=True)