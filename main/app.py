# app.py

from flask import Flask, request , jsonify , render_template , redirect , url_for
from flask_pymongo import PyMongo
from flask_sqlalchemy import SQLAlchemy 
from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import  ChromeDriverManager
import requests
import scrape_gambling
import pymongo

# Crate flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/home"
mongo = PyMongo(app)

# Home Page of website
@app.route('/')
def home():
    statdata = mongo.db.statdata.find_one()
    return render_template("index.html")

@app.route("/")
def index():
 
   # Find one record of data from the dataset
    team_tables = mongo.db.team_tables.find_one()

    # Return template and data
    return render_template("index.html", statdata = team_tables)

@app.route("/scrape")
def scrape():
    statdata = mongo.db.statdata

    # Run the scrape function
    statdata = scrape_stats.scrape()

    # Update the Mongo database using update and upsert = True
    statdata.update({}, statdata, upsert=True)
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)


# /calculations path:

# Win/Losses - determines number of wins, losses, and ties
# Win Percentage - percentage of time a team has won
# Previous Odds - 
# Margin of Victory (Average) - avg margin of victory

# Figuring out if it will be useful to rename and manipulate data here for a table? To get the results?
