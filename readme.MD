# Eating Disneyland
Already confined to overpriced and under-evaluated food options, theme park goers everywhere are one step closer to having their hopes and prayers answered with *Eating Disneyland*, a Google Maps-inspired application for viewing and reviewing all food options around the Disneyland park in Anaheim, CA. 

Anyone can view restaurant details along with all other user-reviews, but of course you must be logged in with an account in order to create a review yourself. 

## Technologies Used
* Python
* Flask
* Jinja2
* PostgreSQL
* SQLAlchemy
* JavaScript
* Axios
* Folium/Leaflet
* Bootstrap

## How to run your own instance of Eating Disneyland:
* Use this branch of Eating_Disneyland: https://github.com/seanthewonderful/Eating_Disneyland.git

* Create a Python Virtual Environment and activate it
* Install all dependencies
    * __pip3 install -r requirements.txt__
* Create a new file in the 'eating' directory, `config.sh`
    * Use the following environment variables to allow flask script and seed_db.py file to run properly: 
    ```python
    export POSTGRES_URI='postgresql:///eating_disneyland'
    export SECRET_KEY='make your own secret key'
    export USER_PW='generic password for all seeded users'
    export FLASK_APP='run.py'
    export FLASK_DEBUG='True'
    ```
* Source this file:
    * `source config.sh`
* Seed the database: 
    * `python3 seed_db.py`
* Run the application: 
    * `flask run`
    * follow the link to your localhost provided in the terminal
* Rate some restaurants!