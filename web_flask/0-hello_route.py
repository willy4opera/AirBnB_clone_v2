#!/usr/bin/python3

"""Here we start the web flask application.

The application listens at 0.0.0.0,  and port 5000.
Routes:
    /: SHOW 'Hello HBNB!'
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Show 'Hello HBNB!'"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
