from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pharmacies.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
SQLALCHEMY_TRACK_MODIFICATIONS = True

db = SQLAlchemy(app)


class Pharmacies(db.Model):
    id = db.Column('pharmacy_id', db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    location = db.Column(db.String(50))
    contact = db.Column(db.String(200))
    longitude = db.Column(db.String(10))
    rating = db.Column(db.DECIMAL)
    latitude = db.Column(db.String(10))


def __init__(self, name, location, contact, rating, latitude, longitude):
    self.name = name
    self.location = location
    self.contact = contact
    self.rating = rating
    self.latitude = latitude
    self.longitude = longitude


db.create_all()

db.session.add(
    Pharmacies(
        name='Steve', location='New York',
        contact='123-456-7890', rating=5,
        latitude='40.7128', longitude='74.0060'
    )
)
db.session.commit()