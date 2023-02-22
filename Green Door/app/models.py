from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
class User(UserMixin, db.Model):
    __tablename__ = 'user'
    
    first_name= db.Column(db.String(20))
    Last_name = db.Column(db.String(20))
    username = db.Column(db.String(30), primary_key=True)
    email = db.Column(db.String(30) )
    password_hash = db.Column(db.String(50))
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

@login.user_loader
def load_user(id):
    return db.session.query(User).get(int(id))