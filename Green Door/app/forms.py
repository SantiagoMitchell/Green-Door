from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField("Submit")

class RegisterForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    show_password = BooleanField('Show password')
    phone_number = StringField('Phone Number', validators=[DataRequired()])
    street_number = StringField('Street Number', validators=[DataRequired()])
    street = StringField('Street', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    state = StringField('State', validators=[DataRequired()])
    zip_code = StringField('Zip Code', validators=[DataRequired()])
    submit = SubmitField("Submit")
class SearchForm(FlaskForm):
    name = StringField('search', validators=[DataRequired()])
    submit = SubmitField("Submit")

class ProfileForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    show_password = BooleanField('Show password')
    phone_number = StringField('Phone Number', validators=[DataRequired()])
    street_number = StringField('Street Number', validators=[DataRequired()])
    street = StringField('Street', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    state = StringField('State', validators=[DataRequired()])
    zip_code = StringField('Zip Code', validators=[DataRequired()])

class CarForm(FlaskForm):
    make = StringField('Make', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    year = StringField('Year', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    website_url = StringField('Website URL', validators=[DataRequired()])
    price = StringField('Price', validators=[DataRequired()])
    battery = BooleanField('Battery')
    certification = StringField('Certification')
    submit = SubmitField('Add Car')

class FoodForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    website_url = StringField('Website URL', validators=[DataRequired()])
    certification = StringField('Certification')
    submit = SubmitField('Add Food')

class ClothingForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    website_url = StringField('Website URL', validators=[DataRequired()])
    price = StringField('Price', validators=[DataRequired()])
    certification = StringField('Certification')
    submit = SubmitField('Add Clothing')

class HotelForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    website_url = StringField('Website URL', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    country = StringField('Country', validators=[DataRequired()])
    certification = StringField('Certification')
    submit = SubmitField('Add Hotel')

