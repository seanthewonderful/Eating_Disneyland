from flask import Flask
from flask_wtf import FlaskForm
from wtforms import (StringField, SubmitField, PasswordField, TextAreaField, EmailField,
                    IntegerField, RadioField, SelectField, BooleanField)
from wtforms.validators import DataRequired, Email, Length, NumberRange, email_validator


class RegisterForm(FlaskForm):
    username = StringField('Username', render_kw={'placeholder':'Unique Username'}, validators=[DataRequired()])
    password = PasswordField('Password', render_kw={'placeholder':'Password'}, validators=[DataRequired()])
    email = EmailField('Email', render_kw={'placeholder':'Email Address'}, validators=[Email()])
    age = IntegerField('Age', render_kw={'placeholder':'Your age'}, validators=[NumberRange(min=8, max=120)])
    zipcode = StringField('Zip Code', render_kw={'placeholder':'Your Zip Code'}, validators=[Length(min=5, max=5, message='Only U.S. zipcodes accepted(5 numbers total)')])
    submit = SubmitField('Submit')
    
class LoginForm(FlaskForm):
    username = StringField('Username', render_kw={'placeholder':'Username'}, validators=[DataRequired()])
    password = PasswordField('Password', render_kw={'placeholder':'Password'}, validators=[DataRequired()])
    submit = SubmitField('Submit')