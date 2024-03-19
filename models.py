from app import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from flask_login import UserMixin


class Logs(db.Model):
    # __tablename__ = "logs"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    info = db.Column(db.String(300))
    date = db.Column(db.DateTime, default=datetime.utcnow())
    type = db.Column(db.String(10), nullable=False)
    # user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    # user = db.relationship("User", back_populates="company")
    user_name = db.Column(db.String(100), nullable=False)
    user_color = db.Column(db.String(10), nullable=False)

    def get_color(self):
        if self.type == "success":
            return "#146B14"
        elif self.type == "error":
            return "#751515"
        elif self.type == "warning":
            return "#757315"

    def __repr__(self):
        return '<Log %r>' % self.id


class Users(db.Model, UserMixin):
    # __tablename__ = "users"
    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    name = db.Column(db.String(100))
    password_hash = db.Column(db.String(100), nullable=False)
    created_on = db.Column(db.DateTime(), default=datetime.utcnow)
    color = db.Column(db.String(10))
    # logs = db.relationship('Logs', backref='user')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)


    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


    def __repr__(self):
        return "<Users %r>" % self.name


class Titles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    path = db.Column(db.String(150),unique=True, nullable=False)
    title = db.Column(db.String(300), nullable=False)

    def __repr__(self):
        return '<Titles %r>' % self.path


class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    path = db.Column(db.String(150),unique=True, nullable=False)
    title = db.Column(db.String(300), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow())
    img1 = db.Column(db.String(150), nullable=False)
    img2 = db.Column(db.String(150), nullable=False)
    def __repr__(self):
        return '<Titles %r>' % self.path