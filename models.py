from flask_sqlalchemy import SQLAlchemy
from werkzeug import generate_password_hash, check_password_hash


db = SQLAlchemy()

class User(db.Model):
	__tablename__ = 'users'
	uid = db.Column(db.Integer, primary_key = True)
	firstname = db.Column(db.String(100))
	lastname = db.Column(db.String(100))
	email = db.Column(db.String(100), unique =  True)
	pwdhash = db.Column(db.String(54))


	def __init__(self,firstname,lastname,email, password):
		self.firstname = firstname.title()
		self.lastname = lastname.title()
		self.email = email.lower()
		self.setpassword(password)

	def setpassword(self, password):
		self.pwdhash = generate_password_hash(password)

	def checkpassword(self, password):
		return check_password_hash(self.pwdhash, password) 