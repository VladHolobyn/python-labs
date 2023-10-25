from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class LoginForm(FlaskForm):
    name = StringField(label='User name')
    password = PasswordField(label='Password')
    submit = SubmitField(label="Sign in")
