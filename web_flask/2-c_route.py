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


@my_app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    display “HBNB”
    """
    return "HBNB"


@my_app.route("/c/<text>", strict_slashes=False)
def C_is_fun(text):
    """
    display “C ” followed by the value of the text
    """
    return "C " + text.replace("_", " ")


if __name__ == "__main__":
    my_app.run(host="0.0.0.0", port=5000)
