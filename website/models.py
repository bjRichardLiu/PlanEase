# Import from current package (website)
# Same as from website import db
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func



class Tasks (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    # foreign key to link to user, if no id, it won't create the note
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

# TODO add other kinds of information of the user

class User(db.Model, UserMixin):
    # create columns for the database
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    firstName = db.Column(db.String(150))
    password = db.Column(db.String(150))
    tasks = db.relationship('Tasks')
