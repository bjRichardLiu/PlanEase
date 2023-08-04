# Import from current package (website)
# Same as from website import db
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func



class Task (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    morning = db.Column(db.Boolean)
    weekdaysOnly = db.Column(db.Boolean)
    deadline = db.Column(db.Integer)
    priority = db.Column(db.Integer)
    timeRequired = db.Column(db.Integer)
    
    # foreign key to link to user, if no id, it won't create the task
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class ReservedTime (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    beginTime = db.Column(db.Integer)
    endTime = db.Column(db.Integer)
    weekdaysOnly = db.Column(db.Boolean)
    # foreign key to link to user, if no id, it won't create the task
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class WakeUpTime (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    weekdays = db.Column(db.Integer)
    weekends = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    # create columns for the database
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    firstName = db.Column(db.String(150))
    password = db.Column(db.String(150))
    tasks = db.relationship('Tasks')
