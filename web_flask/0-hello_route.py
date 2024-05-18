#!/usr/bin/python3
"""
A simple Flask web application.
"""
from flask import Flask

my_app = Flask(__name__)

@my_app.route("/", strict_slashes=False)
def Hello():
    """
    Returns a string 'Hello HBNB!'
    """
    return "Hello HBNB!"

if __name__ == "__main__":
    my_app.run(host="0.0.0.0", port=5000)
