from flask import Flask
from flask import render_template as rt


app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return rt("home.html", user ="Devonte Shendo")

@app.route("/breweries")
def breweries():
    return rt("breweries.html", user ="Devonte Shendo")

@app.route("/beer_types")
def beer_types():
    return rt("beer_types.html", user ="Devonte Shendo")

@app.route("/about")
def hello_world():
    return rt("about.html", user ="Devonte Shendo")

if __name__ == "__main__":
    app.run(debug=True)