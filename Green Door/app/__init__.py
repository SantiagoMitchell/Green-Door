from flask import Flask

# New imports
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from dotenv import load_dotenv
from os import environ
import mysql.connector

# force loading of environment variables
load_dotenv('.flaskenv')

# Get the environment variables from .flaskenv
IP = environ.get('34.173.53.247')
USERNAME = environ.get('csc-400')
PASSWORD = environ.get('Tenclams98')
DB_NAME = environ.get('GreenDoor')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'csc400'

# Specify the connection parameters/credentials for the database
DB_CONFIG_STR = f"mysql+mysqlconnector://{USERNAME}:{PASSWORD}@{IP}/{DB_NAME}"
app.config['SQLALCHEMY_DATABASE_URI'] = DB_CONFIG_STR
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]= True

# Create database connection and associate it with the Flask application
db = SQLAlchemy(app)
login = LoginManager(app)

login.login_view= 'login'
# Add models
from app import routes, models



user = User.query.filter_by(username='admin').first()
if user is None:
    user_admin = User(username='admin', role='admin')
    user_admin.set_password('csc400')
    db.session.add(user_admin)
    db.session.commit()


user = User.query.filter_by(username='user').first()
if user is None:
    username = 'user'
    reg_user = User(username='user', role = 'user')
    reg_user.set_password('csc400')
    db.session.add(reg_user)
    member = Member(member_id=username, group_id=None, eval_id=None)
    db.session.add(member)
    db.session.commit()