"""
main file for the service
"""
from flask import Flask, render_template

app = Flask(__name__)
app.debug = True

@app.route('/')
def welcome():
    return render_template('home.html')