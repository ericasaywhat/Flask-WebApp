from flask import Flask, render_template #importing Flask class

app = Flask(__name__)

#minimal Flask application
@app.route("/") #looks for URL decorator
def main():
	return render_template('index.html')
	# return "Welcome!"

@app.route('/showSignUp')
def showSignUp():
	return render_template('signup.html')

if __name__ == "__main__":
	
	app.run()


