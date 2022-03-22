from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017"
mongo = PyMongo(app)

 # mars.update_one({}, {"$set": mars_data}, upsert=True) From homework solution, will be helpful

if __name__ == "__main__":
    app.run(debug=True)