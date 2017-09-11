"""
main file for the service
"""
from flask import Flask, render_template
from data import OurGuitars

Guitars = OurGuitars()


app = Flask(__name__)
app.debug = True

@app.route('/')
def welcome():
    return render_template('home.html')

@app.route('/about')
def about():return render_template('about.html')

@app.route('/browse')
def browse():return render_template('browse.html', guitars = Guitars)

@app.route('/guitar/<string:ID>')
def viewitem(ID):return render_template('guitar.html', id = ID)