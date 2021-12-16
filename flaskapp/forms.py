from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField,FileField
from wtforms.fields.numeric import IntegerField
from wtforms.validators import DataRequired, Length, Email

class AddForm(FlaskForm):
    company_id = IntegerField('Company',validators=[DataRequired()])
    name = StringField('Name',
                           validators=[DataRequired(), Length(min=2, max=20)])
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=25)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    phone = StringField('Phone',
                        validators=[DataRequired(),Length(min=10, max=10)])
    dob = StringField('DOB',
                        validators=[DataRequired()])
    image_file = FileField('Image')
                            
    submit = SubmitField('Add Employee')