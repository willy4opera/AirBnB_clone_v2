#!/usr/bin/python3

"""Here, we started the Flask web application.

The application listens at 0.0.0.0:5000.
Routes:
    /: Shows 'Hello HBNB!'.
    /hbnb: Displays 'HBNB'.
    /c/<text>: Displays 'C' followed by the value of <text>.
    /python/(<text>): Displays 'Python' followed by the value of <text>.
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """SHow 'Hello HBNB!'."""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displays 'HBNB'."""
    return "HBNB"


@app.route("/c/<txt>", strict_slashes=False)
def c(ext):
    """Show 'C' followed by the value of <text>.

    Replace underscores in <text> with slashes.
    """
    txt = txt.replace("_", " ")
    return "C {}".format(txt)


@app.route("/python", strict_slashes=False)
@app.route("/python/<txt>", strict_slashes=False)
def python(txt="is cool"):
    """Show 'Python' followed by the value of <text>.

    Replace underscores in <text> with slashes.
    """
    txt = txt.replace("_", " ")
    return "Python {}".format(txt)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
