#!/usr/bin/python3

"""Here, we started the Flask web application.

The application listens on 0.0.0.0:5000.
Routes:
    /: Shows 'Hello HBNB!'.
    /hbnb: Shows 'HBNB'.
    /c/<text>: Shows 'C' followed by the value of <text>.
    /python/(<text>): Shows 'Python' followed by the value of <text>.
    /number/<n>: Shows 'n is a number' only if <n> is an integer.
    /number_template/<n>: Displays an HTML page only if <n> is an integer.
        - Shows the value of <n> in the body.
    /number_odd_or_even/<n>: Displays an HTML page only if <n> is an integer.
        - States whether <n> is even or odd in the body.
"""
from flask import Flask
from flask import render_template

app = Flask(__name__)
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Shows 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Shows 'HBNB'"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """Shows 'C' followed by the value of <text>

    Replaces underscores in <text> with slashes.
    """
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """Shows 'Python' followed by the value of <text>

    Replace underscores in <text> with slashes.
    """
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """Shows 'n is a number' only if <n> is an integer."""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """Shows an HTML page only if <n> is an integer.

    Shows the value of <n> in the body.
    """
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    """Shows the HTML page only if <n> is an integer.

    States if <n> is odd or even in the body.
    """
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
