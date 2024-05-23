#!/usr/bin/python3
"""
A simple Flask web application.
"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """
    Displays an HTML page with a list of all State objects present
    in DBStorage,
    sorted by name (A->Z).
    """
    dict_states = storage.all(State)
    all_states = []
    for k, v in dict_states.items():
        all_states.append(v)
    return render_template('7-states_list.html', all_states=all_states)


@app.teardown_appcontext
def teardown_db(self):
    """
    Remove the current SQLAlchemy Session.
    """
    self.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
