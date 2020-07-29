from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import PasswordType, force_auto_coercion
db = SQLAlchemy()

force_auto_coercion()

class Users(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    ign = db.Column(db.Unicode(13), nullable=False)
    discord_id = db.Column(db.Unicode(20), nullable=False)
    mobile_no = db.Column(db.Unicode(10), nullable=False)
    username = db.Column(db.Unicode(20), nullable=False)
    password = db.Column(db.String(), nullable=False)
    team_id = db.Column(db.Integer, db.ForeignKey('teams.id'), nullable=True)
    parent = db.relationship("Teams", back_populates="children")

class Teams(db.Model):
    __tablename__ = "teams"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    team_name = db.Column(db.Unicode(20), nullable=False)
    team_leader = db.Column(db.Unicode(20), nullable=False)
    match_played = db.Column(db.Unicode(10), nullable=False)
    match_id = db.Column(db.Integer, db.ForeignKey('matches.id'), nullable=True)
    children = db.relationship("Users", back_populates="teams")


class Matches(db.Model):
    __tablename__ = "matches"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    play_date = db.Column(db.Unicode(20), nullable=False)
    result = db.Column(db.String(), nullable=False)
    children = db.relationship("Teams")
