from app import app
from flask import render_template, redirect, url_for, request
from flask_login import login_user, logout_user, login_required, current_user
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from werkzeug.security import check_password_hash, generate_password_hash
from app.forms import LoginForm, RegisterForm
from app.forms import LoginForm, RegisterForm
from app import db
from app.models import User
import sys


@app.route('/success')
def loginSuccess():
    return render_template('loginSuccess.html')

@app.route('/login',methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('loginSuccess'))
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.query(User).filter_by(username=form.username.data).first()
        password = request.form['password']
        valid_password = check_password_hash(user.password_hash, password)
        if user is None or not valid_password:
            print('Login failed', file=sys.stderr)
            return render_template('unsuccessfulLogin.html', form=form)
        else:
            login_user(user)
            print('Login successful', file=sys.stderr)
            return redirect(url_for('loginSuccess'))
    return render_template('login.html', form=form)

    
@app.route('/register', methods=['GET', 'POST'])

def register():
    
    form = RegisterForm()
    if request.method== 'POST':
        if form.validate_on_submit():
            user = User.query.filter_by(username=form.username.data).first()
            if user is None:
                first_name = form.first_name.data
                Last_name = form.last_name.data
                username = form.username.data
                email = form.email.data
                password_hash = request.form['password']
                role = 'user'
                user = User(First_name=First_name, Last_name=Last_name, email=email, username=username)
                user.set_password(password)
                db.session.add(user)
                user = db.session.query(User).filter_by(username=form.username.data).first()
                return render_template('registerSuccess.html')
        else:
            return render_template('unsuccessfulLogin.html', form=form)
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

@app.route('/clothingSearchHome')
def clothingsearchhome():
    return render_template('clothingSearchHome.html')

@app.route('/clothingSearchResult')
def clothingsearchresult():
    return render_template('clothingSearchResult.html')

@app.route('/foodSearchHome')
def foodsearchhome():
    return render_template('foodSearchHome.html')

@app.route('/foodSearchResult')
def foodsearchresult():
    return render_template('foodSearchResult.html')

@app.route('/hotelSearchHome')
def hotelsearchhome():
    return render_template('hotelSearchHome.html')

@app.route('/hotelSearchResult')
def hotelsearchresult():
    return render_template('hotelSearchResult.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/siteSearchHome')
def sitesearchhome():
    return render_template('siteSearchHome.html')

@app.route('/siteSearchResults')
def sitesearchresult():
    return render_template('siteSearchResults.html')

