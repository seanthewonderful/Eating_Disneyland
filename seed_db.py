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
        "name": "Gibson Girl Ice Cream Parlor",
        "land": "Main Street",
        "expense": "$",
        "image_url": "https://farm9.static.flickr.com/8421/7763878548_b4dca6cb9b_b.jpg",
        "description": "Disneyland Main Street's nostalgic ice cream parlor & sweet shop with an elaborate old-timey Americana theme.",
        "full_service": False,
        "x_coord": 33.811165,
        "y_coord": -117.919086,
    },
    {
        "name": "Market House",
        "land": "Main Street",
        "expense": "$",
        "image_url": "https://lh3.googleusercontent.com/p/AF1QipP0o24z8tLQuz63ppjHGB0zQoKiU6Tj9_5BUAtx=s680-w680-h510",
        "description": "Disneyland's very own Starbucks.",
        "full_service": False,
        "x_coord": 33.810929374836455,
        "y_coord": -117.91888406625188,
    },
    {
        "name": "Refreshment Corner",
        "land": "Main Street",
        "expense": "$",
        "image_url": "https://allears.net/wp-content/uploads/archive/dining/images/dining_location_image_1970.jpg",
        "description": "Casual Disney stop for quick American fare including hot dogs, pretzels, and desserts.",
        "full_service": False,
        "x_coord": 33.811440,
        "y_coord": -117.919081,
    },
    {
        "name": "Plaza Inn",
        "land": "Main Street",
        "expense": "$$",
        "image_url": "https://www.disneytouristblog.com/wp-content/uploads/2012/03/DSC_7449.jpg",
        "description": "Quick-serve spot in Disneyland featuring a character breakfast buffet, as well as pay-per-item lunch and dinner buffets with themed dishes.",
        "full_service": False,
        "x_coord": 33.8116963939521,
        "y_coord": -117.91851581766903,
    },
    {
        "name": "Little Red Wagon",
        "land": "Main Street",
        "expense": "$",
        "image_url": "https://www.disneytouristblog.com/wp-content/uploads/2014/07/little-red-wagon-disneyland-121.jpg",
        "description": "Counter-service cart serving hand-dipped corn dogs.",
        "full_service": False,
        "x_coord": 33.81148556711443,
        "y_coord": -117.9186905116349,
    },
    {
        "name": "Jolly Holiday Cafe",
        "land": "Main Street",
        "expense": "$$",
        "image_url": "https://www.disneyfoodblog.com/wp-content/uploads/2021/08/2021-disneyland-jolly-holiday-bakery-cafe.jpg",
        "description": "Mary Poppins-inspired cafe serving breakfast and lunch options and desserts.",
        "full_service": False,
        "x_coord": 33.81168285912394,
        "y_coord": -117.9193818473908,
    },
    {
        "name": "Rancho Del Zocalo",
        "land": "Frontierland",
        "expense": "$$",
        "image_url": "https://live.staticflickr.com/7011/6678915119_90248b4eb4_b.jpg",
        "description": "Mexican eatery offering a variety of Mexican dishes in a lively setting with lots of shaded, outdoor seating.",
        "full_service": False,
        "x_coord": 33.81245859568607,
        "y_coord": -117.9199964482139,
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
        "name": "Red Rose Taverne",
        "land": "Fantasyland",
        "expense": "$$$",
        "image_url": "https://www.disneytouristblog.com/wp-content/uploads/2017/03/red-rose-taverne-beauty-beast-restaurant-disneyland-048.jpg",
        "description": "Fantasy-story themed cafe with indoor and outdoor seating featuring American eats inspired from Disney films.",
        "full_service": False,
        "x_coord": 33.81346065509974,
        "y_coord": 117.9194651550013,
    },
    {
        "name": "Pizza Planet",
        "land": "Tomorrowland",
        "expense": "$$",
        "image_url": "https://www.disneyfoodblog.com/wp-content/uploads/2021/07/2021-dl-disneyland-pizza-planet-atmosphere.jpg",
        "description": "Quick-service pizza, pasta, & salad in a colorful, futuristic setting.",
        "full_service": False,
        "x_coord": 33.811728031793685,
        "y_coord": -117.91691154585381,
    },
    {
        "name": "Galactic Grill",
        "land": "Tomorrowland",
        "expense": "$",
        "image_url": "https://i0.wp.com/attractioninsight.com/wp-content/uploads/2022/08/galactic-grill-dlr.jpg?fit=2400%2C1600&quality=100&strip=all&ssl=1",
        "description": "Basic American eats with covered outdoor seating and viewing access to the Jedi Training Academy show.",
        "full_service": False,
        "x_coord": 33.8123815226415,
        "y_coord": -117.91715260949891,
    },
    {
        "name": "Troubadour Tavern",
        "land": "Fantasyland",
        "expense": "$",
        "image_url": "https://www.disneyfoodblog.com/wp-content/uploads/2015/07/TroubadourTavern_15_013.jpg",
        "description": "Sounter-serve snack shack with a Middle-Ages motif & menu with light fare.",
        "full_service": False,
        "x_coord": 33.8144856242707,
        "y_coord": -117.91875940912425,
    },
    {
        "name": "Daisy's Diner",
        "land": "Toontown",
        "expense": "$$",
        "image_url": "https://i1.wp.com/diningatdisney.com/wp-content/uploads/2014/06/DSC01131-d@d.jpg?ssl=1",
        "description": "Daisy Duck-themed walk-up window in Toontown serving pizza, salad, and soda",
        "full_service": False,
        "x_coord": 33.81551618186138,
        "y_coord": -117.91871838555176,
    },
    {
        "name": "Pluto's Doghouse",
        "land": "Toontown",
        "expense": "$",
        "image_url": "https://farm3.static.flickr.com/2823/9874579363_c1c487a0d9_b.jpg",
        "description": "Walk-up window serving picnic baskets with a variety of options, geared toward kids.",
        "full_service": False,
        "x_coord": 33.81554960890238,
        "y_coord": -117.91871033892531,
    },
    {
        "name": "Clarabelle's",
        "land": "Toontown",
        "expense": "$",
        "image_url": "https://i.ytimg.com/vi/op2ovjXYyTo/maxresdefault.jpg",
        "description": "Toontown's own hand-scooped ice cream from a walk-up window.",
        "full_service": False,
        "x_coord": 33.81557802187698,
        "y_coord": -117.91868821070254,
    },
    {
        "name": "Milk Stand",
        "land": "Galaxy's Edge",
        "expense": "$$",
        "image_url": "https://static.wikia.nocookie.net/starwars/images/3/3d/Milk-Stand.png/revision/latest?cb=20211204202414",
        "description": "Cool down with an icy cup of blue or green milk inspired by the Star Wars universe.",
        "full_service": False,
        "x_coord": 33.814428886234296,
        "y_coord": -117.92069637808706,
    },
    {
        "name": "Olga's Cantina",
        "land": "Galaxy's Edge",
        "expense": "$$$",
        "image_url": "https://blogmickey.com/wp-content/uploads/2019/06/ogas-cantina-review-interior-1.jpg",
        "description": "Star Wars-themed bar featuring quirky cocktails (with and without alcohol), snacks, and a droid for a DJ.",
        "full_service": True,
        "x_coord": 33.8147258031444,
        "y_coord": -117.920964585531,
    },
    {
        "name": "Docking Bay 7 Food and Cargo",
        "land": "Galaxy's Edge",
        "expense": "$$",
        "image_url": "https://www.disneytouristblog.com/wp-content/uploads/2019/07/docking-bay-7-food-cargo-star-wars-galaxys-edge-disney-counter-service-restaurant-234.jpg",
        "description": "Spacious hangar with a generic Star Wars spaceport theme serving informal international eats such as noodles and ribs.",
        "full_service": False,
        "x_coord": 33.81469267859092,
        "y_coord": -117.92147272989884,
    },
    {
        "name": "Ronto Roasters",
        "land": "Galaxy's Edge",
        "expense": "$$",
        "image_url": "https://ziggyknowsdisney.com/wp-content/uploads/2019/10/ronto-roasters-galaxys-edge-11-pod-racing-engine-800x533.jpg",
        "description": "Counter-serve option for intergalactic pork or vegetarian wraps.",
        "full_service": False,
        "x_coord": 33.814462613156586,
        "y_coord": -117.92153869443413,
    },
    {
        "name": "Hungry Bear",
        "land": "Critter Country",
        "expense": "$",
        "image_url": "https://farm4.static.flickr.com/3821/12143478353_43313610fa_b.jpg",
        "description": "Rustic, counter-serve option featuring traditional American fare with lots of covered, outdoor seating overlooking the Rivers of America.",
        "full_service": False,
        "x_coord": 33.812590935972715,
        "y_coord": -117.92260721018377,
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
    {
        "name": "Mint Julep Bar",
        "land": "New Orleans Square",
        "expense": "$$",
        "image_url": "https://www.disneyfoodblog.com/wp-content/uploads/2013/07/Mint-Julep-Bar.jpg",
        "description": "Old-timey, New Orleans-themed walk-up window for nonalcoholic cocktails and espresso drinks, as well as beignets.",
        "full_service": False,
        "x_coord": 33.811182398373205,
        "y_coord": -117.92166376575899,
    },
    {
        "name": "French Market Restaurant",
        "land": "New Orlean's Square",
        "expense": "$$",
        "image_url": "https://www.disneyland4ever.com/uploads/2/4/8/5/24855797/719057659.jpg",
        "description": "New Orleans-themed eatery with Southern fare, counter service, and a covered, garden patio.",
        "full_service": False,
        "x_coord": 33.81125204155685,
        "y_coord": -117.92162085041623,
    },
    {
        "name": "Cafe Orleans",
        "land": "New Orleans Square",
        "expense": "$$$",
        "image_url": "https://www.disneytouristblog.com/wp-content/uploads/2014/01/disneyland-christmas-2013-069.jpg",
        "description": "Classic restaurant featuring Cajun & Creole specialties in casual surrounds with a patio.",
        "full_service": True,
        "x_coord": 33.811243684377416,
        "y_coord": -117.92120041416223,
    },
    {
        "name": "Blue Bayou Restaurant",
        "land": "New Orleans Square",
        "expense": "$$$$",
        "image_url": "https://i.pinimg.com/originals/48/2f/54/482f54c4b7e39c2f00314efb98daf13f.jpg",
        "description": "Evocative Cajun-style restaurant set inside the Pirates of the Caribbean ride with an outdoor, nighttime bayou ambience.",
        "full_service": True,
        "x_coord": 33.811113869426435,
        "y_coord": -117.9210944669072,
    },
    {
        "name": "Royal Street Veranda",
        "land": "New Orlean's Square",
        "expense": "$",
        "image_url": "https://www.ocregister.com/wp-content/uploads/migration/o0k/o0k397-b88517818z.120160106161000000gn7ctph7.20.jpg?w=978",
        "description": "Counter-service window serving Cajun-style soups in bread bowls.",
        "full_service": False,
        "x_coord": 33.811242012942394,
        "y_coord": -117.92095096871431,
    },
    {
        "name": "River Belle Terrace",
        "land": "Frontierland",
        "expense": "$$$",
        "image_url": "https://www.wdwinfo.com/wp-content/uploads/2018/12/IMG_6009.jpg",
        "description": "Antebellum-style eatery with a riverfront terrace for Southern dining",
        "full_service": True,
        "x_coord": 33.81149662796846,
        "y_coord": -117.92051108644743,
    },
    {
        "name": "Bengal Barbecue",
        "land": "Adventureland",
        "expense": "$$",
        "image_url": "https://static.wikia.nocookie.net/junglecruise/images/d/dc/9877129093_fe24e00648_b.jpg",
        "description": "Counter-serve spot featuring grilled meat & veggie skewers and other casual, jungle eats.",
        "full_service": False,
        "x_coord": 33.81154732802444,
        "y_coord": -117.92031126189028,
    },
    {
        "name": "Stage Door Cafe",
        "land": "Frontierland",
        "expense": "$",
        "image_url": "https://www.ocregister.com/wp-content/uploads/migration/o0k/o0k3m7-b88517821z.120160106161829000g84crc77.20.jpg?w=1024",
        "description": "Fast-food outpost serving hand-dipped corn dogs, chicken tenders, and funnel cakes.",
        "full_service": False,
        "x_coord": 33.81189888473691,
        "y_coord": -117.9203206496091,
    },
    {
        "name": "Golden Horseshoe",
        "land": "Frontierland",
        "expense": "$",
        "image_url": "https://www.disneytouristblog.com/wp-content/uploads/2015/04/golden-horseshoe-disneyland-night.jpg",
        "description": "Quick-serve saloon serving fish 'n' chips, ice cream, and chicken strips with live Western music shows.",
        "full_service": False,
        "x_coord": 33.812048755541824,
        "y_coord": -117.9202844397871,
    },
    {
        "name": "Turkey Leg Cart",
        "land": "Frontierland",
        "expense": "$$",
        "image_url": "https://www.disneyfoodblog.com/wp-content/uploads/2014/03/Frontierland-Turkey-leg-Cart-2.jpg",
        "description": "Cart offering Disneyland's classic, gigantic, smoked turkey legs.",
        "full_service": False,
        "x_coord": 33.812423735113434,
        "y_coord": -117.92057041285449,
    },
    {
        "name": "Maurice's Treats",
        "land": "Fantasyland",
        "expense": "$",
        "image_url": "https://diningatdisney.com/wp-content/uploads/2013/07/Maurices-Treats.jpg",
        "description": "Beauty and the Beast themed wagon offering savory and sweet pastries and fruit-flavored frozen drinks.",
        "full_service": False,
        "x_coord": 33.81250160079871,
        "y_coord": -117.91931709893191,
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
