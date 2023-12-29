#!/usr/bin/python3

"""Here, we started the Flask web application.

The application listens at 0.0.0.0:5000.
Routes:
    /: Shows 'Hello HBNB!'.
    /hbnb: Displays 'HBNB'.
    /c/<text>: Displays 'C' followed by the value of <text>.
    /python/(<txt>): Displays 'Python' followed by the value of <text>.
    /number/<n>: Displays 'n is a number' only if <n> is an integer.
"""
from flask import Flask
from flask import abort

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Shows 'Hello HBNB!'."""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Shows 'HBNB'."""
    return "HBNB"


@app.route("/c/<txt>", strict_slashes=False)
def c(txt):
    """Shows 'C' followed by the value of <text>.

    Replaces any underscores in <text> with slashes.
    """
    txt = txt.replace("_", " ")
    return "C {}".format(txt)


@app.route("/python", strict_slashes=False)
@app.route("/python/<txt>", strict_slashes=False)
def python(txt="is cool"):
    """Shows 'Python' followed by the value of <txt>.

    Replace underscores in <txt> with slashes.
    """
    txt = txt.replace("_", " ")
    return "Python {}".format(txt)


@app.route("/number/<int:num>", strict_slashes=False)
def number(num):
    """Shows 'num is a number' only if n is an integer."""
    return "{} is a number".format(num)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
