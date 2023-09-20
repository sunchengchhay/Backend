from app.extenstions import db


class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Integer, unique=True)
    email = db.Column(db.String(100), unique=True)
    password_hash = db.Column(db.String(150))
    created_at = db.Column(db.DateTime)
