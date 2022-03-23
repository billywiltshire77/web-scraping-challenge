from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017"
mongo = PyMongo(app)

@app.route("/scrape")
def home():

    # Find one record of data from the mongo database
    

 # mars.update_one({}, {"$set": mars_data}, upsert=True) From homework solution, will be helpful

if __name__ == "__main__":
    app.run(debug=True)