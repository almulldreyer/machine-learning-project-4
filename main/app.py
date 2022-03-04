# app.py

from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import scrape_stats
import requests


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
    ATLt2 = mongo.db.ATLt2.find_one()

    # Return template and data
    return render_template("index.html", statdata = ATLt2)

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

