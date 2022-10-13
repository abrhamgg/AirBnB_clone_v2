#!/usr/bin/python3
"""Basic flask app"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    return "Hello HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
