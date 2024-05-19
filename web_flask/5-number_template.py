#!/usr/bin/python3
"""
A simple Flask web application.
"""
from flask import Flask, render_template

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


@my_app.route("/python/", defaults={'text': 'is cool'}, strict_slashes=False)
@my_app.route("/python/<text>", strict_slashes=False)
def python_is_fun(text):
    """
    display “Python ”, followed by the value of the text
    """
    return "Python " + text.replace("_", " ")


@my_app.route("/number/<int:num>", strict_slashes=False)
def number(num):
    return f"{num} is a number"


@my_app.route("/number_template/<int:num>", strict_slashes=False)
def num_temp(num):
    return render_template('5-number.html', number=num)


if __name__ == "__main__":
    my_app.run(host="0.0.0.0", port=5000)
