from flask import Flask, render_template

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


@app.route('/')
def index():
	return 'Welcome to Flask App'


if __name__ == '__main__':
	app.run(debug=True)