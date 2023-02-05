from model import Restaurant, User, Rating, Fountain, FountainRating, Cuisine, connect_to_db, db
import os


cuisines = ["Breakfast", "American", "Southern", "Mexican", "Italian", "Dessert", "Snacks", "Coffee", "Alcohol", "Intergalactic"]
users = []


os.system("source config.sh")

for cuisine in cuisines:
    new_cuisine = Cuisine(cuisine)
    db.session.add(cuisine)
    
db.session.commit()
