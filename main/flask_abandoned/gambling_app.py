from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_sports

# Crate flask
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/phone_app"
mongo = PyMongo(app)

# Or set inline
# mongo = PyMongo(app, uri="mongodb://localhost:27017/phone_app")


@app.route("/")
def index():
    atltables = mongo.db.atltables.find_one()
    return render_template("index.html", atltables =  )


@app.route("/scrape_info")
def scraper():
    atltables = mongo.db.atltables
    atl_data = atltables.scrape()
    atltables.update({}, atl_data, upsert=True)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)