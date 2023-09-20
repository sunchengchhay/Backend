from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy

api = Api(version='1.0', title='API Document',
          description='API for System Design')
db = SQLAlchemy()
