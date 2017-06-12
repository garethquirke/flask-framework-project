"""
main file for the service
"""
from flask import Flask

app = Flask(__name__)

@app.route('/')
def welcome():
    return 'welcome to the site'
