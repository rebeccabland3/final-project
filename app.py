# import necessary libraries
# from models import create_classes
import os
from flask import Flask, render_template, jsonify, request, redirect
from sqlalchemy import create_engine
import pandas as pd

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Database Setup
#################################################

from flask_sqlalchemy import SQLAlchemy


# # db = SQLAlchemy(app)
db = create_engine("sqlite:///data/species_database.sqlite")

# create route that renders index.html template
@app.route("/")
def home():

    return render_template("index.html")

@app.route("/api/tracks")
def species():
    sql = "select * from tracks"
    species_df = pd.read_sql(sql = sql, con = db)

    species_results = species_df.to_json(orient = "records")
    
    return jsonify(species_results)

if __name__ == "__main__":
    app.run()
