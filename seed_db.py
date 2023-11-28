from eating.model import (
    Restaurant,
    User,
    Rating,
    Fountain,
    FountainRating,
    Cuisine,
    connect_to_db,
    db,
)
from eating import app
from werkzeug.security import generate_password_hash
import os

os.system("source config.sh")
os.system("dropdb eating_disneyland")
os.system("createdb eating_disneyland")

app.app_context().push()

db.create_all()
print("Tables created...")

cuisines = [
    "Breakfast",
    "American",
    "Southern",
    "Mexican",
    "Italian",
    "Dessert",
    "Snacks",
    "Coffee",
    "Alcohol",
    "Intergalactic",
]

users = [
    {
        "username": "tinytim",
        "password": generate_password_hash(
            os.environ["USER_PW"], method="pbkdf2:sha256", salt_length=8
        ),
        "email": "t@t.com",
        "age": 40,
        "zipcode": 92692,
    },
    {
        "username": "myquizowski",
        "password": generate_password_hash(
            os.environ["USER_PW"], method="pbkdf2:sha256", salt_length=8
        ),
        "email": "mw@mw.com",
        "age": 18,
        "zipcode": 84045,
    },
    {
        "username": "larrythelarry",
        "password": generate_password_hash(
            os.environ["USER_PW"], method="pbkdf2:sha256", salt_length=8
        ),
        "email": "l@l.com",
        "age": 65,
        "zipcode": 92692,
    },
]

restaurants = [
    {
        "name": "Carnation Cafe",
        "land": "Main Street",
        "expense": "$$$",
        "image_url": "https://static.wikia.nocookie.net/disney/images/6/65/Carnation_Cafe_2012.png",
        "description": "Dine on classic American comfort food, including some of Walt’s favorite dishes, at this Main Street, U.S.A. institution.",
        "full_service": True,
        "x_coord": 33.811067,
        "y_coord": -117.919103,
    },
    {
        "name": "Edelweiss Snacks",
        "land": "Fantasyland",
        "expense": "$",
        "image_url": "https://static.wikia.nocookie.net/disney/images/4/48/EdelweissSnacksExterior.jpg",
        "description": "Visit this alpine chalet where you’ll be happy to meet turkey legs, chimichangas and buttered corn on the cob. Then, chill out in the shadow of the Matterhorn with a fountain drink or frozen beverage in blue raspberry, cherry or apple.",
        "full_service": False,
        "x_coord": 33.81374305708073,
        "y_coord": -117.91774430413204,
    },
    {
        "name": "Harbour Galley",
        "land": "Critter Country",
        "expense": "$$",
        "image_url": "https://blog-cdn.touringplans.com/blog/wp-content/uploads/2021/12/IMG_5040.jpg",
        "description": "Drop anchor along the waterfront and stop by this swell seafood shanty for a quick meal that’ll set your taste buds afloat.",
        "full_service": False,
        "x_coord": 33.812041180621804,
        "y_coord": -117.9219757109676,
    },
]

fountains = [
    {
        "name": "Red Rose Tavern Fountain",
        "land": "Fantasyland",
        "image_url": "red_rose.png",
        "description": "In the olden times I was left to myself for most of the day, but since the contruction of Galaxy's Edge I can't begin to tell you how many humans must exist on this planet. It might even be in the millions. Come say hi so I can add you to the human tally.",
        "x_coord": 33.813555095191816,
        "y_coord": -117.91969266601622,
    },
    {
        "name": "River Belle Terrace Fountain",
        "land": "Frontierland",
        "image_url": "river_belle.png",
        "description": "Elegantly aged, I sit in front of the River Belle Terrace seating area, facing Pirate Island. Without much relief from the sun, my water isn't often very cool, but grab yourself a cup of ice and come fill up!",
        "x_coord": 33.81179993283393,
        "y_coord": -117.92053414788177,
    },
    {
        "name": "Small World Fountain",
        "land": "Fantasyland",
        "image_url": "small_world.png",
        "description": "Unassiming and practical, I enjoy occasional peace and quiet simply because of how few people know I exist.",
        "x_coord": 33.814428366540696,
        "y_coord": -117.91849157457128,
    },
]

os.system("source config.sh")

for cuisine in cuisines:
    new_cuisine = Cuisine(name=cuisine)
    db.session.add(new_cuisine)

print("Cuisine table done")

for user in users:
    new_user = User(
        username=user["username"],
        password=user["password"],
        email=user["email"],
        age=user["age"],
        zipcode=user["zipcode"],
    )
    db.session.add(new_user)

print("User table done")

for restaurant in restaurants:
    new_restaurant = Restaurant(
        name=restaurant["name"],
        land=restaurant["land"],
        expense=restaurant["expense"],
        image_url=restaurant["image_url"],
        description=restaurant["description"],
        full_service=restaurant["full_service"],
        x_coord=restaurant["x_coord"],
        y_coord=restaurant["y_coord"],
    )
    db.session.add(new_restaurant)

print("Restaurant table done")

for fountain in fountains:
    new_fountain = Fountain(
        name=fountain["name"],
        land=fountain["land"],
        image_url=fountain["image_url"],
        description=fountain["description"],
        x_coord=fountain["x_coord"],
        y_coord=fountain["y_coord"],
    )
    db.session.add(new_fountain)

db.session.commit()

cc_rating = Rating(
    star_rating=4,
    review="Lively location on Main Street.",
    restaurant=Restaurant.query.filter_by(name="Carnation Cafe").first(),
    user=db.session.get(User, 1),
)
es_rating = Rating(
    star_rating=5,
    review="I love to come here for an authentic Swiss chimichanga.",
    restaurant=Restaurant.query.filter_by(name="Edelweiss Snacks").first(),
    user=db.session.get(User, 2),
)
hg_rating = Rating(
    star_rating=5,
    review="Great place for a snack, hidden in plain sight.",
    restaurant=Restaurant.query.filter_by(name="Harbour Galley").first(),
    user=db.session.get(User, 3),
)

rrtf_rating = FountainRating(
    star_rating=5,
    review="I love taking a sip near the Red Rose",
    user=db.session.get(User, 1),
    fountain=Fountain.query.filter_by(name="Red Rose Tavern Fountain").first(),
)
rbtf_rating = FountainRating(
    star_rating=4,
    review="It's truly warm water, but the locale is lovely.",
    user=db.session.get(User, 2),
    fountain=Fountain.query.filter_by(name="River Belle Terrace Fountain").first(),
)
swf_rating = FountainRating(
    star_rating=5,
    review="Sometimes I loiter here to absord the peace and quiet, and to have a constant water flow.",
    user=db.session.get(User, 3),
    fountain=Fountain.query.filter_by(name="Small World Fountain").first(),
)

db.session.add_all(
    [cc_rating, es_rating, hg_rating, rrtf_rating, rbtf_rating, swf_rating]
)
db.session.commit()

print("Ratings created")

print("Database successfully seeded.")
