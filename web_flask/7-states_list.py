#!/usr/bin/python3
"""Basic flask app"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """Displays Hello HBNB"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Display HBNB"""
    return "HBNB"


@app.route('/c/<string:text>', strict_slashes=False)
def cIsFun(text):
    """accepts a string argument as input"""
    text = text.replace('_', ' ')
    return "C {}".format(text)


@app.route('/python', strict_slashes=False)
@app.route('/python/<string:text>', strict_slashes=False)
def python_is_cool(text="is cool"):
    """accepts string input from the url"""
    text = text.replace('_', ' ')
    print(text)
    return "Python {}".format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """displays n if only n is int"""
    if type(n) is int:
        return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def num(n):
    """render html page"""
    if type(n) is int:
        return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def num_type(n):
    """render html page"""
    if type(n) is int:
        return render_template('6-number_odd_or_even.html', n=n)


@app.route('/states_list', strict_slashes=False)
def state_list():
    """list states"""
    state = storage.all("State")
    state_list = {}
    for k, v in state.items():
        k = k.split('.')[1]
        state_list[k] = v.name
    print(state_list)
    sorted_state = dict(sorted(state_list.items(), key=lambda item: item[1]))
    return render_template('7-states_list.html', state_list=sorted_state)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
