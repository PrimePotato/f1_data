from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/f1.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Circuit(db.Model):
    __tablename__ = 'circuits'
    circuitId = db.Column(db.Integer, primary_key=True)
    circuitRef = db.Column(db.String(255))
    name = db.Column(db.String(255))
    location = db.Column(db.String(255))
    country = db.Column(db.String(255))
    lat = db.Column(db.Float)
    lng = db.Column(db.Float)
    alt = db.Column(db.Integer)
    url = db.Column(db.String(255))


class DriverStanding(db.Model):
    __tablename__ = 'driver_standings'
    driverStandingsId = db.Column(db.Integer, primary_key=True)
    raceId = db.Column(db.Integer)
    driverId = db.Column(db.Integer)
    points = db.Column(db.Float)
    position = db.Column(db.Integer)
    positionText = db.Column(db.String(255))
    wins = db.Column(db.Integer)


class Driver(db.Model):
    __tablename__ = 'drivers'
    driverId = db.Column(db.Integer, primary_key=True)
    driverRef = db.Column(db.Integer)
    number = db.Column(db.Integer)
    code = db.Column(db.Float)
    forename = db.Column(db.Integer)
    surname = db.Column(db.String(255))
    dob = db.Column(db.Integer)
    nationality = db.Column(db.String(255))
    url = db.Column(db.String(255))


class Race(db.Model):
    __tablename__ = 'races'
    raceId = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer)
    round = db.Column(db.Integer)
    circuitId = db.Column(db.Integer)
    name = db.Column(db.String(255))
    date = db.Column(db.Date)
    time = db.Column(db.Time)
    url = db.Column(db.String(255))


class Qualifying(db.Model):
    qualifyId = db.Column(db.Integer, primary_key=True)
    raceId = db.Column(db.Integer)
    driverId = db.Column(db.Integer)
    constructorId = db.Column(db.Integer)
    number = db.Column(db.Integer)
    position = db.Column(db.Integer)
    q1 = db.Column(db.String(255))
    q2 = db.Column(db.String(255))
    q3 = db.Column(db.String(255))


class Result(db.Model):
    __tablename__ = 'results'
    resultId = db.Column(db.Integer, primary_key=True, nullable=False, default=None)
    raceId = db.Column(db.Integer, nullable=False, default=0)
    driverId = db.Column(db.Integer, nullable=False, default=0)
    constructorId = db.Column(db.Integer, nullable=False, default=0)
    number = db.Column(db.Integer, nullable=True, default=None)
    grid = db.Column(db.Integer, nullable=False, default=0)
    position = db.Column(db.Integer, nullable=True, default=None)
    positionText = db.Column(db.String(255), nullable=False, default=None)
    positionOrder = db.Column(db.Integer, nullable=False, default=0)
    points = db.Column(db.Integer, nullable=False, default=0)
    laps = db.Column(db.Integer, nullable=False, default=0)
    time = db.Column(db.String(255), nullable=True, default=None)
    milliseconds = db.Column(db.Integer, nullable=True, default=None)
    fastestLap = db.Column(db.Integer, nullable=True, default=None)
    rank = db.Column(db.Integer, nullable=True, default=0)
    fastestLapTime = db.Column(db.String(255), nullable=True, default=None)
    fastestLapSpeed = db.Column(db.String(255), nullable=True, default=None)
    statusId = db.Column(db.Integer, nullable=False, default=0)
