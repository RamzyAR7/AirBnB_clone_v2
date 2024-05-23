#!/usr/bin/python3
"""
A simple Flask web application.
"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception=None):
    """
    Remove the current SQLAlchemy Session.
    """
    storage.close()


@app.route("/cities_by_states", strict_slashes=False)
def states_list():
    """
    Displays an HTML page with a list of all State objects present
    in DBStorage,
    sorted by name (A->Z).
    Display a HTML page with the list of states"""
    states = storage.all(State).values()
    return render_template('8-cities_by_states.html', states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
