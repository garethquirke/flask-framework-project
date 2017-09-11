"""
main file for the service
"""
from flask import Flask, render_template, flash, redirect, url_for, session, logging
from data import OurGuitars
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt

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