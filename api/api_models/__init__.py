from flask_restx import fields

from api.extenstions import api

login_model = api.model(
    "Login",
    {
        "username": fields.String(required=True),
        "password": fields.String(required=True),
    },
)

register_model = api.model(
    "Register",
    {
        "username": fields.String(required=True),
        "email": fields.String(required=True),
        "password": fields.String(required=True),
    },
)
