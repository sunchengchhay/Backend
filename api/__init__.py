from flask import Flask
from flask_cors import CORS

from api.extenstions import api, db
from api.resources import ns


def create_app():

    app = Flask(__name__)

    # config app
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"

    # Initialize CORS with default settings
    CORS(app,
         # Replace with your frontend's domain
         origins=["localhost:3000"],
         supports_credentials=True,  # Allows cookies and HTTP authentication
         # Whitelist headers)
         allow_headers=["Content-Type", "application/json"],
         )
    # init extentions
    api.init_app(app)
    db.init_app(app)

    # Create database table
    with app.app_context():
        db.create_all()

    # register namespace
    api.add_namespace(ns)

    return app
