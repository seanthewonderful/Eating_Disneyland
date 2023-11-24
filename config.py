from os import environ


class Config:
    SECRET_KEY = environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = environ.get("POSTGRES_URI")
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASK_DEBUG = True
    USER_PW = environ.get("USER_PW")
    FLASK_APP = environ.get("FLASK_APP")
