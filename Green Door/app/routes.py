from app import app
from flask import render_template, redirect, url_for
from app.forms import AddForm, DeleteForm, SearchForm
from app import db
import sys

@app.route('/')
def hello():
    return render_template('homepage.html')