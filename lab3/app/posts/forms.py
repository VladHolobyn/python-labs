from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField 
from wtforms import StringField, TextAreaField, RadioField, BooleanField, SubmitField, SelectField, SelectMultipleField
from wtforms.validators import DataRequired
from .models import EnumPriority

class PostForm(FlaskForm):
    title = StringField(label='Title', validators=[DataRequired("Title is required")])
    text = TextAreaField(label='Text', validators=[DataRequired("Text is required")])
    image = FileField(label='Image', validators=[FileAllowed(['jpg','png'])])
    type = RadioField(label='Priority', choices=[
        (EnumPriority.low.value, EnumPriority.low.name),
        (EnumPriority.medium.value, EnumPriority.medium.name),
        (EnumPriority.high.value, EnumPriority.high.name)], 
        default='2')
    enabled= BooleanField(label='Show post')
    categories = SelectField(label="Category", coerce=int)
    tags = SelectMultipleField(label="Tags", coerce=int)
    submit = SubmitField(label="Save")

class CategoryForm(FlaskForm):
    name = StringField(label='Name', validators=[DataRequired("Name is required")])
    submit = SubmitField(label="Save category")

class TagForm(FlaskForm):
    name = StringField(label='Name', validators=[DataRequired("Name is required")])
    submit = SubmitField(label="Save tag")

class SearchForm(FlaskForm):
    category = SelectField(label="Category", coerce=int, choices=[(-1,'all')], default=-1)
    submit = SubmitField(label="Search")
