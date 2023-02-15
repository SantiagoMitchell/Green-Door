from app import app
from flask import render_template, redirect, url_for
from app.forms import AddForm, DeleteForm, SearchForm
from app import db
import sys

@app.route('/')
def hello():
    return render_template('homepage.html')

@app.route('/about')
def hello():
    return render_template('about.html')

@app.route('/clothingSearchHome')
def hello():
    return render_template('clothingSearchHome.html')

@app.route('/clothingSearchResult')
def hello():
    return render_template('clothingSearchResult.html')

@app.route('/foodSearchHome')
def hello():
    return render_template('foodSearchHome.html')

@app.route('/foodSearchResult')
def hello():
    return render_template('foodSearchResult.html')

@app.route('/hotelSearchHome')
def hello():
    return render_template('hotelSearchHome.html')

@app.route('/hotelSearchResult')
def hello():
    return render_template('hotelSearchResult.html')

@app.route('/login')
def hello():
    return render_template('login.html')

@app.route('/profile')
def hello():
    return render_template('profile.html')

@app.route('/siteSearchHome')
def hello():
    return render_template('siteSearchHome.html')

@app.route('/siteSearchResults')
def hello():
    return render_template('siteSearchResults.html')

