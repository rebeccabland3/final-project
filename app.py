# import necessary libraries
# from models import create_classes
import os
from flask import Flask, render_template, jsonify, request, redirect
import pandas as pd



#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Database Setup
#################################################

# create route that renders index.html template
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/visualizations")
def visualizations():
    return render_template("visualizations.html")

if __name__ == "__main__":
    app.run()
