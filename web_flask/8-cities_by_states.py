#!/usr/bin/python3

"""Here, we started the Flask web application.

The application listens at 0.0.0.0:5000.
Routes:
    /cities_by_states: This HTML page is with a list of all states
    and related cities.
"""

from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.teardown_appcontext
def shutdown_session(exception=None):
    """Here, we reload storage after each request
    """
    storage.close()


@app.route("/cities_by_states", strict_slashes=False)
def states_cities_list():
    """list states and cities sorted by name
    """
    d_states = list(storage.all("State").values())
    d_states.sort(key=lambda x: x.name)
    for state in d_states:
        state.cities.sort(key=lambda x: x.name)
    return render_template('8-cities_by_states.html', states=d_states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
