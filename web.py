from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")
def index():
	return "hey,YOU"
if __name__=="__main__":
	app.debug=True
	app.run()

