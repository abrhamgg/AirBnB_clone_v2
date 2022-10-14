#!/usr/bin/python3
"""Basic flask app"""

from flask import Flask

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


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
