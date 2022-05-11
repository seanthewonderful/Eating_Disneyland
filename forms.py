from flask import Flask
from flask_wtf import FlaskForm
from wtforms import (StringField, SubmitField, PasswordField, TextAreaField, EmailField,
                    IntegerField, RadioField, SelectField, BooleanField)
from wtforms.validators import DataRequired, Email, Length, NumberRange, email_validator


class RegisterForm(FlaskForm):
    username = StringField('username', render_kw={'placeholder':'Unique Username'}, validators=[DataRequired()])
    password = PasswordField('password', render_kw={'placeholder':'Password'}, validators=[DataRequired()])
    email = EmailField('email', render_kw={'placeholder':'Email Address (for account recovery)'}, validators=[Email()])
    age = IntegerField('age', render_kw={'placeholder':'Your age please'}, validators=[NumberRange(min=8, max=120)])
    zipcode = IntegerField('zipcode', render_kw={'placeholder':'Your Zip Code'}, validators=[Length(min=5, max=5, message='Only U.S. zipcodes accepted(5 numbers total)')])
    submit = SubmitField('Submit')
    
class LoginForm(FlaskForm):
    username = StringField('username', render_kw={'placeholder':'Unique Username'}, validators=[DataRequired()])
    password = PasswordField('password', render_kw={'placeholder':'Password'}, validators=[DataRequired()])
    submit = SubmitField('submit')