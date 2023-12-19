from marshmallow import validate, validates_schema, ValidationError
from marshmallow.fields import String
from ...extensions import ma
from app.auth.models import User

class UserSchema(ma.SQLAlchemyAutoSchema):
    username = String(required=True, validate=[validate.Length(min=4, max=14), validate.Regexp(regex='^[A-Za-z][A-Za-z0-9_.]*$')])
    email = String(required=True, validate=[validate.Email()])
    password = String(load_only=True, required=True, validate=[validate.Length(min=7)])

    @validates_schema
    def validate_username(self, data, **kwargs):
        username = data.get('username')

        if User.query.filter_by(username=username).count():
            raise ValidationError(f"Username {username} allready exists")

    @validates_schema
    def validate_email(self, data, **kwargs):
        email = data.get('email')

        if User.query.filter_by(email=email).count():
            raise ValidationError(f'Email {email} already exists')


    class Meta:
        model=User
        load_instance=True
        exclude=['password_hash']
