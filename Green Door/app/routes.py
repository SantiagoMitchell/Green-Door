from app import app
from flask import render_template, redirect, url_for, request
from flask_login import login_user, logout_user, login_required, current_user
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from sqlalchemy import or_
from werkzeug.security import check_password_hash, generate_password_hash
from app.forms import LoginForm, RegisterForm, SearchForm, ProfileForm
from app.forms import LoginForm, RegisterForm, SearchForm, ProfileForm
from app import db
from app.models import User, Food, Clothing, Hotel, Car
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
        user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
        if user:
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
            user = User(first_name=first_name, last_name=last_name, password=password, email=email, username=username, role='user')
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
    if form.validate_on_submit():
        keyword = form.name.data
        # Query all records in the DB table matching the keyword in name or description
        record = db.session.query(Clothing).filter(
            or_(
                Clothing.name.ilike(f"%{keyword}%"),
                Clothing.description.ilike(f"%{keyword}%")
            )
        ).all()
        if record:
            return render_template('clothingSearchResult.html', clothing=record)
        else:
            return render_template('about.html')
    return render_template('clothingSearchHome.html', form=form)
@app.route('/clothingSearchResult')
def clothingsearchresult():
    return render_template('clothingSearchResult.html')

@app.route('/foodSearchHome', methods=['GET', 'POST'])
def foodsearchhome():
    form = SearchForm()
    if form.validate_on_submit():
        keyword = form.name.data
        # Query all records in the DB table matching the keyword in name or description
        record = db.session.query(Food).filter(
            or_(
                Food.name.ilike(f"%{keyword}%"),
                Food.description.ilike(f"%{keyword}%")
            )
        ).all()
        if record:
            return render_template('foodSearchResult.html', foods=record)
        else:
            return render_template('about.html')
    return render_template('foodSearchHome.html', form=form)

@app.route('/foodSearchResult')
def foodsearchresult():
    return render_template('foodSearchResult.html')

@app.route('/hotelSearchHome', methods=['GET', 'POST'])
def hotelsearchhome():
    form = SearchForm()
    if form.validate_on_submit():
        keyword = form.name.data
        # Query all records in the DB table matching the keyword in name or description
        record = db.session.query(Hotel).filter(
            or_(
                Hotel.name.ilike(f"%{keyword}%"),
                Hotel.description.ilike(f"%{keyword}%")
            )
        ).all()
        if record:
            return render_template('hotelSearchResult.html', hotels=record)
        else:
            return render_template('about.html')
    return render_template('hotelSearchHome.html', form=form)

@app.route('/hotelSearchResult')
def hotelsearchresult():
    return render_template('hotelSearchResult.html')

@app.route('/profile', methods=['GET', 'POST'])
def profile():
    form = ProfileForm()
    if request.method == 'GET':
        form.first_name.data = current_user.first_name
        form.last_name.data = current_user.last_name
        form.email.data = current_user.email
        form.username.data = current_user.username
    return render_template('profile.html', form=form)

@app.route('/carSearchHome', methods=['GET', 'POST'])
def carsearchhome():
    form = SearchForm()
    if form.validate_on_submit():
        keyword = form.name.data
        # Query all records in the DB table matching the keyword in make, name, or description
        record = db.session.query(Car).filter(
            or_(
                Car.make.ilike(f"%{keyword}%"),
                Car.name.ilike(f"%{keyword}%"),
                Car.description.ilike(f"%{keyword}%")
            )
        ).all()
        if record:
            return render_template('carSearchResult.html', cars=record)
        else:
            return render_template('about.html')
    return render_template('carSearchHome.html', form=form)

@app.route('/carSearchResults')
def carsearchresult():
    return render_template('carSearchResult.html')

