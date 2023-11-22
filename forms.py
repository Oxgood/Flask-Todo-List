from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SubmitField
from wtforms.validators import DataRequired


class TodoForms(FlaskForm):
    todo_name = StringField('Todo name', validators=[DataRequired()])
    todo_date = DateField('', validators=[DataRequired()])
    todo_add = SubmitField('Add')
