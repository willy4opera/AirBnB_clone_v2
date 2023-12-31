#!/usr/bin/python3

"""Here, we started the simple flask app
"""

from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.teardown_appcontext
def shutdown_session(exception=None):
    """Here, we reload storage after each request
    """
    storage.close()


@app.route("/states_list", strict_slashes=False)
def states_list():
    """list states sorted by name
    """
    d_states = list(storage.all("State").values())
    d_states.sort(key=lambda x: x.name)
    Text = render_template('7-states_list.html', states=d_states)
    return Text


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
