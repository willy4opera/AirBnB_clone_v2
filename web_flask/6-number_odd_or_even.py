#!/usr/bin/python3

"""Here, we defined a simple flask app
"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """"/" defines the root route
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """hbnb
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def cisfun(text):
    """c what
    """
    Text = "C {}".format(text.replace('_', ' '))
    return Text


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def pythoniscool(text='is cool'):
    """python is cool
    """
    Text = "Python {}".format(text.replace('_', ' '))
    return Text


@app.route("/number/<int:n>", strict_slashes=False)
def intnumber(n):
    """accept integer
    """
    Text = "{} is a number".format(n)
    return Text


@app.route("/number_template/<int:n>", strict_slashes=False)
def int_template(n):
    """only renders if n is integer
    """
    Text = render_template('5-number.html', number=n)
    return Text


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def odd_or_even(n):
    """Only renders when n is integer
    """
    Text = render_template('6-number_odd_or_even.html', number=n)
    return Text


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
