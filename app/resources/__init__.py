from flask_restx import Resource, Namespace
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from flask import request
import pytz

from app.models import User
from app.extenstions import db
from app.api_models import register_model, login_model

ns = Namespace("Authentication",
               description="Authentication endpoint", path="/auth")
desired_timezone = pytz.timezone('Asia/Phnom_Penh')


@ns.route("/register")
class Register(Resource):

    @ns.expect(register_model)
    def post(self):
        """Register a new user"""
        data = ns.payload or request.json
        username = data["username"]
        email = data["email"]
        password_hash = generate_password_hash(data["password"])
        created_at = datetime.now(pytz.utc).astimezone(desired_timezone)

        # Check if the username or email already exists
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            return {"message": "Username already exists"}, 400

        existing_email = User.query.filter_by(email=email).first()
        if existing_email:
            return {"message": "Email already exists"}, 400

        user = User(username=username, email=email,
                    password_hash=password_hash, created_at=created_at)
        db.session.add(user)
        db.session.commit()

        return {"message": "User registered successfully"}, 201


@ns.route("/login")
class LoginResource(Resource):
    @ns.expect(login_model)
    def post(self):
        """User login"""
        data = ns.payload or request.json
        username = data["username"]
        password = data["password"]

        # Find the user by username
        user = User.query.filter_by(username=username).first()

        # Check if the user exists and the password is correct
        if user and check_password_hash(user.password_hash, password):
            # Generate an access token (you can customize this)
            # access_token = create_access_token(
            #     identity=user.id, expires_delta=datetime.timedelta(days=1))
            return {"message": "login successfully"}, 200
        else:
            return {"message": "Invalid username or password"}, 401
