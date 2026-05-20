from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()


class User(UserMixin, db.Model):

    id = db.Column(db.Integer, primary_key=True)

    full_name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    phone = db.Column(db.String(20))

    password = db.Column(db.String(100))

    role = db.Column(db.String(20))

    profession = db.Column(db.String(100))
    experience = db.Column(db.String(100))
    charges = db.Column(db.String(50))

    def __repr__(self):
        return f'<User {self.full_name}>'