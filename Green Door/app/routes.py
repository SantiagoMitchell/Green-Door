from app import app
from flask import render_template, redirect, url_for
import sys

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

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/siteSearchHome')
def sitesearchhome():
    return render_template('siteSearchHome.html')

@app.route('/siteSearchResults')
def sitesearchresult():
    return render_template('siteSearchResults.html')

