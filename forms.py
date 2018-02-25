from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class SignupForm(Form):
	first_name = StringField('First Name', validators=[DataRequired('Please enter your first name')])
	last_name = StringField('Last Name',validators=[DataRequired('Please enter your last name')])
	email = StringField('Email',validators=[DataRequired('Please enter your email'), Email('Please enter valid email')])
	password = PasswordField('Password',validators=[DataRequired('Please enter your password'),Length(min=6,message='Enter minium 6 characters')])
	submit = SubmitField('Sign Up')
	
