from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash



class User(UserMixin, db.Model):
    __tablename__ = 'users'
    username = db.Column(db.String(255), primary_key=True)
    password = db.Column(db.String(255))
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)
    role = db.Column(db.String(255))
    phone_number = db.Column(db.String(20))
    street_number = db.Column(db.String(20))
    street = db.Column(db.String(255))
    city = db.Column(db.String(255))
    state = db.Column(db.String(255))
    zip_code = db.Column(db.String(10))

    def get_id(self):
        return str(self.username)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, pwd):
        return check_password_hash(self.password, pwd)
    
class Food(db.Model):
    __tablename__ = 'foods'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    description = db.Column(db.Text)
    website_url = db.Column(db.String(255))
    certification = db.Column(db.String(255))


class Clothing(db.Model):
    __tablename__ = 'clothing'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    description = db.Column(db.Text)
    website_url = db.Column(db.String(255))
    price = db.Column(db.Float)
    certification = db.Column(db.String(255))


class Hotel(db.Model):
    __tablename__ = 'hotels'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    description = db.Column(db.Text)
    website_url = db.Column(db.String(255))
    city = db.Column(db.String(255))
    country = db.Column(db.String(255))
    certification = db.Column(db.String(255))


class Car(db.Model):
    __tablename__ = 'cars'
    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(255))
    name = db.Column(db.String(255))
    year = db.Column(db.Integer)
    description = db.Column(db.Text)
    website_url = db.Column(db.String(255))
    price = db.Column(db.Float)
    battery = db.Column(db.Boolean)
    certification = db.Column(db.String(255))

@login.user_loader
def load_user(id):
    return User.query.get(id)