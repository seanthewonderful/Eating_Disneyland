from flask import Flask
from flask_wtf.csrf import CSRFProtect
from jinja2 import StrictUndefined
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config

csrf = CSRFProtect()
db = SQLAlchemy()
login_manager = LoginManager()


def create_app(config_class=Config):
    app = Flask(__name__)

    import os

    os.system("source config.sh")

    app.config.from_object(config_class)

    csrf.init_app(app)
    with app.app_context():
        db.init_app(app)
    login_manager.init_app(app)
    app.jinja_env.undefined = StrictUndefined

    from eating.blueprints.auth.routes import auth_bp
    from eating.blueprints.errors.handlers import errors
    from eating.blueprints.fountains.routes import fountains_bp
    from eating.blueprints.main.routes import main
    from eating.blueprints.maps.routes import map_bp
    from eating.blueprints.restaurants.routes import restaurants_bp
    from eating.blueprints.users.routes import users_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(errors)
    app.register_blueprint(fountains_bp)
    app.register_blueprint(main)
    app.register_blueprint(map_bp)
    app.register_blueprint(restaurants_bp)
    app.register_blueprint(users_bp)

    return app
