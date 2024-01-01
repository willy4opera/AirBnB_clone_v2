#!/usr/bin/python3

"""Here, we started the simple flask app
"""

from flask import Flask, render_template
from models import storage
from os import environ as env
app = Flask(__name__)


@app.teardown_appcontext
def shutdown_session(exception=None):
    """Here, we reploaded storage after each request
    """
    storage.close()


@app.route("/states/<id>", strict_slashes=False)
@app.route("/states", strict_slashes=False)
def states_cities_list(id=None):
    """Here, we display state and cities if id is given
    otherwise list all states
    """
    d_states = storage.all("State")
    if id:
        state = d_states.get('State.{}'.format(id))
        d_states = [state] if state else []
    else:
        d_states = list(d_states.values())
    d_states.sort(key=lambda x: x.name)
    for state in d_states:
        state.cities.sort(key=lambda x: x.name)
    return render_template(
        '9-states.html',
        states=d_states,
        len=len(d_states),
        id=id
    )


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
