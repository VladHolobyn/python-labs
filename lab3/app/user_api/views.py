from flask_restful import Resource
from app.auth.models import User
from ..extensions import db
from flask_restful import reqparse


parser_create_user = reqparse.RequestParser()
parser_create_user.add_argument('username', type=str, required=True, help='Username is required')
parser_create_user.add_argument('email', type=str, required=True, help='Email is required')
parser_create_user.add_argument('password', type=str, required=True, help='Password is required')
parser_create_user.add_argument('confirm_password', type=str, required=True, help='Confirem password is required')


class UsersApi(Resource):
    def get(self):
        # returns pageable users
        pass
    
    def post(self):
        # Creates new user
        pass
        # data = parser_create_user.parse_args()
        # username = data.get('username')
        # email = data.get('email')
        # password = data.get('password')
        # confirm_password = data.get('confirm_password')

        # new_user = User(name=username, password=password, email=email)

        # db.session.add(new_user)
        # db.session.commit()

        # return {'message': 'User has been created'}, 201

class UserApi(Resource):
    def get(self):
        # returns user by id
        pass
    
    def put(self):
        # updates user
        pass
    
    def delete(self):
        # delete user
        pass

