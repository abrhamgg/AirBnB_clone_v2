#!/usr/bin/python3
"""Starts a flask app
    listens to 0.0.0.0:5000
"""
from models import storage
from flask import Flask
from models.state import State
from models.city import City
from flask import render_template

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def states_list():
    """Displays an HTML page with a list of all State objects in DBStorage.
    States are sorted by name.
    """
    states = storage.all(State).values()
    cities = storage.all(City).values()
    states = sorted(states, key=lambda k: k.name)
    cities = sorted(cities, key=lambda k: k.name)
    print(cities)
    return render_template("8-cities_by_states.html",
                           states=states, cities=cities)


@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
