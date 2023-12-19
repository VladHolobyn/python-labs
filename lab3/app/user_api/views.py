from flask import request
from flask_restful import Resource
from flask_restful import reqparse
from app.auth.models import User
from ..extensions import db
from .schemas.user import UserSchema


class UsersApi(Resource):
    def get(self):
        schema = UserSchema(many=True)
        users = User.query.all()
        return {"users": schema.dump(users)}
    
    def post(self):
        schema = UserSchema()

        new_user = schema.load(request.json)
        db.session.add(new_user)
        db.session.commit()

        return {'user': schema.dump(new_user)}, 201

class UserApi(Resource):
    def get(self, id):
        schema = UserSchema()
        user = User.query.filter_by(id=id).first_or_404()
        return {"user": schema.dump(user)}

    
    def put(self, id):
        schema = UserSchema(partial=True)
        user = User.query.filter_by(id=id).first_or_404()
        
        user = schema.load(request.json, instance=user)
        db.session.add(user)
        db.session.commit()
        
        return {"user": schema.dump(user)}
    
    def delete(self, id):
        schema = UserSchema()
        user = User.query.filter_by(id=id).first_or_404()
        
        db.session.delete(user)
        db.session.commit()
        
        return {"user": schema.dump(user)}
