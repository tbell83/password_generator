from flask import Flask
from flask import render_template
import passwd_gen

app = Flask(__name__)

@app.context_processor
def utility_processor():
	def get_pass():
		return passwd_gen.generate_password()
	return dict(get_pass=get_pass)

@app.route('/')
def root():
	return render_template('index.html')

@app.route('/password')
def password():
	return render_template('password.html')

if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0')
