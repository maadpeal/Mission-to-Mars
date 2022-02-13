from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import scraping
from config import user, password, database

app = Flask(__name__)

app.config["MONGO_URI"] = f"mongodb://{user}:{password}@172.20.0.1:27017/{database}"
mongo = PyMongo(app)

@app.route("/")
def index():
   mars = mongo.db.mars.find_one()
   return render_template("index.html", mars=mars)

@app.route("/scrape")
def scrape():
   mars = mongo.db.mars
   mars_data = scraping.scrape_all()
   mars.update_one({}, {"$set":mars_data}, upsert=True)
   return redirect('/', code=302)

if __name__ == "__main__":
   app.run()