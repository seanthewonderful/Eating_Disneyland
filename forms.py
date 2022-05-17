from decimal import Decimal
from flask import Flask
from flask_wtf import FlaskForm
from wtforms import (StringField, SubmitField, PasswordField, TextAreaField, EmailField, DecimalField,
                    IntegerField, RadioField, SelectField, BooleanField)
from wtforms.validators import DataRequired, Email, Length, NumberRange, email_validator, InputRequired, EqualTo, ValidationError


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
    
class UpdateUser(FlaskForm):
    username = StringField('Username', render_kw={'placeholder':'Unique Username'}, validators=[DataRequired()])
    password = PasswordField('Password', render_kw={'placeholder':'Password'}, validators=[DataRequired()])
    email = EmailField('Email', render_kw={'placeholder':'Email Address'}, validators=[Email()])
    age = IntegerField('Age', render_kw={'placeholder':'Your age'}, validators=[NumberRange(min=8, max=120)])
    zipcode = StringField('Zip Code', render_kw={'placeholder':'Your Zip Code'}, validators=[Length(min=5, max=5, message='Only U.S. zipcodes accepted(5 numbers total)')])
    submit = SubmitField('Submit')
    
class DeleteUser(FlaskForm):
    type_delete = StringField("Please type DELETE:", validators=[InputRequired()])
    def validate_type_delete(form, field):
        if field.data != 'DELETE':
            raise ValidationError('You must type DELETE in all upper case')
    submit = SubmitField('Submit')
    
class AddRestaurant(FlaskForm):
    name = StringField('Name')
    image_url = StringField('Image URL')
    land = RadioField('Land', choices=['Main Street', 'Adventureland', 'New Orleans Square', 'Critter Country', "Galaxy's Edge", 'Frontierland', 'Fantasyland', "Mickey's Toontown", 'Tomorrowland'])
    expense = SelectField('Expense', choices=[('$', '$'), ('$$', '$$'), ('$$$', '$$$'), ('$$$$', '$$$$')])
    full_service = BooleanField('Full Service')
    breakfast = BooleanField('Breakfast')
    american = BooleanField('American')
    southern = BooleanField('Southern')
    mexican = BooleanField('Mexican')
    italian = BooleanField('Italian')
    dessert = BooleanField('Dessert')
    snacks = BooleanField('Snacks')
    coffee = BooleanField('Coffee')
    beverage_only = BooleanField('Beverage Only')
    x_coord = DecimalField('X Coordinate')
    y_coord = DecimalField('Y Coordinate')
    submit = SubmitField('Submit')