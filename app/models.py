import string
import random
from datetime import datetime
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
CHARACTERS = string.ascii_lowercase + string.digits + string.ascii_uppercase


class ShortCodes(db.Model):
    __tablename__ = "shortcodes"

    def shortId(self):
        return "".join(random.choice(CHARACTERS) for x in range(8))

    id = db.Column(db.Integer, primary_key=True)
    full = db.Column(db.String(200), nullable=False)
    short = db.Column(db.String(8), unique=True, nullable=False, default=shortId)
    clicks = db.Column(db.Integer, nullable=False, default=0)
    created = db.Column(db.DateTime, unique=False, nullable=False, default=datetime.now)

    def __repr__(self):
        return "<id {}>".format(self.id)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(64), nullable=False)

    def __repr__(self):
        return "<User {}>".format(self.username)
