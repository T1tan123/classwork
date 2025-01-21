from enum import unique

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    avatars = db.Column(db.String(200))
    actual_avatars = db.Column(db.String(100))
    likes = db.Column(db.Integer)
    #posts =
    #followers =


