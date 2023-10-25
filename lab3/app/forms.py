from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):
    name = StringField(label='User name', validators=[DataRequired("User name is required")])
    password = PasswordField(label='Password', validators=[
            DataRequired("Password is required"), 
            Length(min=4, max=10, message="Min length - 4, max - 10 symbols")
        ])
    remember = BooleanField(label="Remember me")
    submit = SubmitField(label="Sign in")
