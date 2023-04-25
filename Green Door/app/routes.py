import random
from app import app
from flask import render_template, redirect, url_for, request
from flask_login import login_user, logout_user, login_required, current_user
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from sqlalchemy import or_
from werkzeug.security import check_password_hash, generate_password_hash
from app.forms import LoginForm, RegisterForm, SearchForm, ProfileForm, CarForm, FoodForm, ClothingForm, HotelForm
from app import db
from app.models import User, Food, Clothing, Hotel, Car
from validate_email import validate_email
import phonenumbers
import datetime
import sys


@app.route('/success')
def loginSuccess():
    return render_template('loginSuccess.html')


@app.route('/login',methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('about'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            print('Login successful')
            return render_template('about.html', form=form)
        else:
            print('Login failed')
            return render_template('unsuccessfulLogin.html', form=form)
    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None:
            first_name = form.first_name.data
            last_name = form.last_name.data
            email = form.email.data
            username = form.username.data
            password = form.password.data
            role = 'user'
            phone_number = form.phone_number.data
            street_number = form.street_number.data
            street = form.street.data
            city = form.city.data
            state = form.state.data
            zip_code = form.zip_code.data
            user = User(first_name=first_name, last_name=last_name, password=generate_password_hash(password),
                        email=email, username=username, role=role, phone_number=phone_number, street_number=street_number,
                        street=street, city=city, state=state, zip_code=zip_code)
            db.session.add(user)
            db.session.commit()
            return render_template('registerSuccess.html')
        if user is not None:
            return render_template('unsuccessfulRegister.html', form=form)
    return render_template('register.html', form=form)
	
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/')
def hello():
    return render_template('homepage.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/clothingSearchHome', methods=['GET', 'POST'])
def clothingsearchhome():
    form = SearchForm()
    message = "Please enter a keyword to search." # Set a default message
    if form.validate_on_submit():
        keyword = form.name.data
        # Query all records in the DB table matching the keyword in name or description
        record = db.session.query(Clothing).filter(
            or_(
                Clothing.name.ilike(f"%{keyword}%"),
                Clothing.description.ilike(f"%{keyword}%"),
                Clothing.certification.ilike(f"%{keyword}%")
            )
        ).all()
        if record:
            return render_template('clothingSearchResult.html', clothing=record)
        else:
            message = "Sorry, we couldn't find any results for your search."
    return render_template('clothingSearchHome.html', form=form, message=message)

@app.route('/clothingSearchResult')
def clothingsearchresult():
    return render_template('clothingSearchResult.html')

@app.route('/clothingSearchCert')
def clothingSearchCert():
    records = db.session.query(Clothing).filter(Clothing.certification.isnot(None)).all()
    return render_template('clothingSearchCert.html', clothing=records)

@app.route('/clothingSearchCertAbout')
def clothingSearchCertAbout():
    return render_template('clothingSearchCertAbout.html')


@app.route('/foodSearchHome', methods=['GET', 'POST'])
def foodsearchhome():
    form = SearchForm()
    message = "Please enter a keyword to search." # Set a default message
    if form.validate_on_submit():
        keyword = form.name.data
        # Query all records in the DB table matching the keyword in name or description
        record = db.session.query(Food).filter(
            or_(
                Food.name.ilike(f"%{keyword}%"),
                Food.description.ilike(f"%{keyword}%"),
                Food.certification.ilike(f"%{keyword}%")
            )
        ).all()
        if record:
            return render_template('foodSearchResult.html', foods=record)
        else:
            message = "Sorry, we couldn't find any results for your search."
    return render_template('foodSearchHome.html', form=form, message=message)

@app.route('/foodSearchResult')
def foodsearchresult():
    return render_template('foodSearchResult.html')

@app.route('/foodSearchCert')
def foodSearchCert():
    records = db.session.query(Food).filter(Food.certification.isnot(None)).all()
    return render_template('foodSearchCert.html', foods=records)

@app.route('/foodSearchCertAbout')
def foodSearchCertAbout():
    return render_template('foodSearchCertAbout.html')

@app.route('/hotelSearchHome', methods=['GET', 'POST'])
def hotelsearchhome():
    form = SearchForm()
    message = "Please enter a keyword to search." # Set a default message
    if form.validate_on_submit():
        keyword = form.name.data
        # Query all records in the DB table matching the keyword in name or description
        record = db.session.query(Hotel).filter(
            or_(
                Hotel.name.ilike(f"%{keyword}%"),
                Hotel.description.ilike(f"%{keyword}%"),
                Hotel.city.ilike(f"%{keyword}%"),
                Hotel.country.ilike(f"%{keyword}%"),
                Hotel.certification.ilike(f"%{keyword}%")
            )
        ).all()
        if record:
            return render_template('hotelSearchResult.html', hotels=record)
        else:
            message = "Sorry, we couldn't find any results for your search."
    return render_template('hotelSearchHome.html', form=form, message=message)
@app.route('/hotelSearchResult')
def hotelsearchresult():
    return render_template('hotelSearchResult.html')

@app.route('/hotelSearchCert')
def hotelSearchCert():
    records = db.session.query(Hotel).filter(Hotel.certification.isnot(None)).all()
    return render_template('hotelSearchCert.html', hotels=records)

@app.route('/hotelSearchCertAbout')
def hotelSearchCertAbout():
    return render_template('hotelSearchCertAbout.html')
	
@app.route('/profile', methods=['GET', 'POST'])
def profile():
    form = ProfileForm()
    if request.method == 'GET':
        form.first_name.data = current_user.first_name
        form.last_name.data = current_user.last_name
        form.email.data = current_user.email
        form.username.data = current_user.username
        form.phone_number.data = current_user.phone_number
        form.street_number.data = current_user.street_number
        form.street.data = current_user.street
        form.city.data = current_user.city
        form.state.data = current_user.state
        form.zip_code.data = current_user.zip_code
    return render_template('profile.html', form=form)
@app.route('/carSearchHome', methods=['GET', 'POST'])
def carsearchhome():
    form = SearchForm()
    message = "Please enter a keyword to search." # Set a default message
    if form.validate_on_submit():
        keyword = form.name.data
        # Query all records in the DB table matching the keyword in make, name, description, or certification
        record = db.session.query(Car).filter(
            or_(
                Car.make.ilike(f"%{keyword}%"),
                Car.name.ilike(f"%{keyword}%"),
                Car.description.ilike(f"%{keyword}%"),
                Car.certification.ilike(f"%{keyword}%")
            )
        ).all()
        if record:
            return render_template('carSearchResult.html', cars=record)
        else:
            message = "Sorry, we couldn't find any results for your search."
    return render_template('carSearchHome.html', form=form, message=message)

@app.route('/carSearchResults')
def carsearchresult():
    return render_template('carSearchResult.html')

@app.route('/carSearchEPA')
def carsearchEPA():
    records = db.session.query(Car).filter(Car.certification.isnot(None)).all()
    return render_template('carSearchEPA.html', cars=records)

@app.route('/carSearchEPAAbout')
def carsearchEPAAbout():
    return render_template('carSearchEPAAbout.html')

@app.route('/carSearchBattery')
def carsearchBattery():
    cars = Car.query.filter_by(battery=True).all()
    return render_template('carSearchBattery.html', cars=cars)

@app.route('/carSearchBatteryAbout')
def carsearchBatteryAbout():
    return render_template('carSearchBatteryAbout.html')

@app.route('/adminHome')
def adminHome():
    return render_template('adminHome.html')

@app.route('/adminCar', methods=['GET', 'POST'])
def adminCar():
    form = CarForm()
    error = None
    if form.validate_on_submit():
        car = Car(
            id=random.randint(10000, 99999),
            make=form.make.data,
            name=form.name.data,
            year=form.year.data,
            description=form.description.data,
            website_url=form.website_url.data,
            price=form.price.data,
            battery=form.battery.data,
            certification=form.certification.data
        )
        db.session.add(car)
        db.session.commit()
        return redirect(url_for('adminCar'))
    elif request.method == 'POST':
        error = 'Please fill out all required fields'
    return render_template('adminCar.html', form=form, error=error)


@app.route('/adminClothing', methods=['GET', 'POST'])
def adminClothing():
    form = ClothingForm()
    error = None
    if form.validate_on_submit():
        clothing = Clothing(
            id=random.randint(10000, 99999),
            name=form.name.data,
            description=form.description.data,
            website_url=form.website_url.data,
            price=form.price.data,
            certification=form.certification.data
        )
        db.session.add(clothing)
        db.session.commit()
        return redirect(url_for('adminClothing'))
    elif request.method == 'POST':
        error = 'Please fill out all required fields'
    return render_template('adminClothing.html', form=form, error=error)


@app.route('/adminHotel', methods=['GET', 'POST'])
def adminHotel():
    form = HotelForm()
    error = None
    if form.validate_on_submit():
        hotel = Hotel(
            id=random.randint(10000, 99999),
            name=form.name.data,
            description=form.description.data,
            website_url=form.website_url.data,
            city=form.city.data,
            country=form.country.data,
            certification=form.certification.data
        )
        db.session.add(hotel)
        db.session.commit()
        return redirect(url_for('adminHotel'))
    elif request.method == 'POST':
        error = 'Please fill out all required fields'
    return render_template('adminHotel.html', form=form, error=error)


@app.route('/adminFood', methods=['GET', 'POST'])
def adminFood():
    form = FoodForm()
    error = None
    if form.validate_on_submit():
        food = Food(
            id=random.randint(10000, 99999),
            name=form.name.data,
            description=form.description.data,
            website_url=form.website_url.data,
            certification=form.certification.data
        )
        db.session.add(food)
        db.session.commit()
        return redirect(url_for('adminFood'))
    elif request.method == 'POST':
        error = 'Please fill out all required fields'
    return render_template('adminFood.html', form=form, error=error)