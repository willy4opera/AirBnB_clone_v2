#!/usr/bin/python3

"""Here, we started the Flask web application.

The application listens at 0.0.0.0:5000.
Routes:
    /: Shows 'Hello HBNB!'.
    /hbnb: Displays 'HBNB'.
    /c/<txt>: Shows 'C' followed by the value of <txt>.
    /python/(<txt>): Displays 'Python' followed by the value of <txt>.
    /number/<num>: Displays 'num is a number' only if <n> is an integer.
    /number_template/<num>: Displays an HTML page only if <num> is an integer.
"""
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displays 'HBNB'"""
    return "HBNB"


@app.route("/c/<txt>", strict_slashes=False)
def c(txt):
    """Shows 'C' followed by the value of <text>

    Replace underscores in <txt> with slashes.
    """
    txt = txt.replace("_", " ")
    return "C {}".format(txt)


@app.route("/python", strict_slashes=False)
@app.route("/python/<txt>", strict_slashes=False)
def python(txt="is cool"):
    """Shows 'Python' followed by the value of <txt>

    Replace underscores in <txt> with slashes.
    """
    txt = txt.replace("_", " ")
    return "Python {}".format(txt)


@app.route("/number/<int:num>", strict_slashes=False)
def number(num):
    """Displays 'n is a number' only if <n> is an integer."""
    return "{} is a number".format(num)


@app.route("/number_template/<int:num>", strict_slashes=False)
def number_template(num):
    """Displays an HTML page only if <n> is an integer."""
    return render_template("5-number.html", num=num)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
