from flask import Blueprint
from flask_restful import Api
from .views import UserApi, UsersApi

user_api_bp = Blueprint('user_api', __name__)
api = Api(user_api_bp)

api.add_resource(UsersApi, '/users')
api.add_resource(UserApi, '/users/<int:id>')
