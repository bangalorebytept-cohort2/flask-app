from flask import Flask, render_template, url_for, request, session, url_for, redirect
from models import db, User
from forms import SignupForm


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/learningflask'
app.secret_key = 'development-key'

db.init_app(app)

@app.route('/home')
def home():
	return render_template('home.html')


@app.route('/')
def index():
	return render_template('index.html')

@app.route('/signup',methods=['GET','POST'])
def signup():
	form = SignupForm()
	
	if request.method == 'POST':
		if form.validate() == False:
			return render_template('signup.html', form=form)
		else:
			newuser = User(form.first_name.data, form.last_name.data, form.email.data, form.password.data)
			db.session.add(newuser)
			db.session.commit()

			session['email'] = newuser.email

			return redirect(url_for('home'))

	elif request.method == 'GET':
		return render_template('signup.html',form=form)

if __name__ == '__main__':
	app.run(debug=True)