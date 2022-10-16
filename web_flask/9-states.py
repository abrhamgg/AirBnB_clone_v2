#!/usr/bin/python3
"""Starts a flask app
    listens to 0.0.0.0:5000
"""
from models import storage
from flask import Flask
from models.state import State
from flask import render_template

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states_list():
    """Displays an HTML page with a list of all State objects in DBStorage.
    States are sorted by name.
    """
    states = storage.all(State).values()
    states = sorted(states, key=lambda k: k.name)
    return render_template("7-states_list.html", states=states)


@app.route("/states/<string:id>", strict_slashes=False)
def state_by_id(id):
    """Displays html page found with a list of states found by
    the input"""
    states_id = storage.all(State).keys()
    cities = storage.all("City").values()
    cities = sorted(cities, key=lambda k: k.name)
    state_cities = []
    for city in cities:
        if id == city.state_id:
            state_cities.append(city)
    found = 0
    for state in storage.all(State).values():
        if id == state.id:
            found = 1
    return render_template("9-states.html", states_id=states_id,
                           state_cities=state_cities,
                           id=id, found=found)


@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
