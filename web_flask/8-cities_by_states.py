#!/usr/bin/python3
"""
A simple Flask web application.
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """
    Displays an HTML page with a list of all State objects present
    in DBStorage,
    sorted by name (A->Z).
    Display a HTML page with the list of states"""
    states = storage.all(State).values()
    cities = storage.all(City).values()
    
    return render_template('7-states_list.html', states=states, cities=cities)

@app.teardown_appcontext
def teardown_db(exception):
    """
    Remove the current SQLAlchemy Session.
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
