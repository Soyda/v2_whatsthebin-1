from flask_login import UserMixin
from . import db
 #we add UserMixin to the model in order to add flask_login attributes to the model so that Flask-Login will be able to work with it.
class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

