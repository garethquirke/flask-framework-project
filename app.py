"""
main file for the service
"""

from flask import Flask, render_template
# name : __main__
app = Flask(__name__)
app.debug = True

@app.route('/')
def welcome():
    # return 'gonch'
    return render_template('home.html')