from flask import Flask

# New imports
from flask_sqlalchemy import SQLAlchemy
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

# Add models
from app import routes