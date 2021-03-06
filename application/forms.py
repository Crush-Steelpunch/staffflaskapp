from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, ValidationError

class StaffForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    subjectID = SelectField("Subjects", choices = [])
    submit = SubmitField('Add')

class SubjectAdd(FlaskForm):
    name = StringField("Subject Name", validators=[DataRequired()])
    submit = SubmitField('Add')

