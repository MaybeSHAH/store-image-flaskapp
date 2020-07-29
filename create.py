import os

from flask import Flask, render_template, request
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgres://uorkrxpbgvqofx:dde70522a104a351fd8286e4abdecbb16002a9bf0fc32fe36c28f312206937fd@ec2-3-231-16-122.compute-1.amazonaws.com:5432/d5if5qrhpq83qb'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():
    db.create_all()

if __name__ == "__main__":
    with app.app_context():
        main()
