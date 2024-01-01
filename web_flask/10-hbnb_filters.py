#!/usr/bin/python3

"""Here, we defined the hbnb filter
"""
from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.teardown_appcontext
def shutdown_session(exception=None):
    """reload storage after each request
    """
    storage.close()


@app.route("/hbnb_filters", strict_slashes=False)
def states_cities_list():
    """Here, we pass states and cities sorted by name
    and amenities
    """
    d_states = list(storage.all("State").values())
    d_states.sort(key=lambda x: x.name)
    for state in d_states:
        state.cities.sort(key=lambda x: x.name)
    amenities = list(storage.all("Amenity").values())
    amenities.sort(key=lambda x: x.name)
    Temp_render = render_template(
        '10-hbnb_filters.html',
        states=d_states,
        amenities=amenities
    )
    return Temp_render


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
