"""
main file for the service
"""
from flask import Flask, request, render_template, flash, redirect, url_for, session, logging
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

class RegisterForm(Form):
    name = StringField('Name', [validators.Length(min=1,max=30)])
    username = StringField('Username', [validators.Length(min=5,max=20)])
    email = StringField('Email', [validators.Length(min=6,max=30)])
    password = PasswordField('Password',
     [validators.DataRequired(),
      validators.EqualTo('confirm', message="passwords do not match")
      ])
    confirm = PasswordField('Confirm Password')


@app.route('/register', methods=['GET','POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        return render_template('register.html')
    return render_template('register.html', form=form)