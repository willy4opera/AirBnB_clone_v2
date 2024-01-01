#!/usr/bin/python3

"""Here, we defined hbnb filter
"""
from flask import Flask, render_template, Markup
from models import storage
import sys
app = Flask(__name__)


@app.teardown_appcontext
def shutdown_session(exception=None):
    """Here, we reloaded the storage after each request
    """
    storage.close()


@app.route("/hbnb", strict_slashes=False)
def states_cities_list():
    """Here, we passed the states and cities sorted by name
    and amenities
    """
    d_states = list(storage.all("State").values())
    d_states.sort(key=lambda x: x.name)
    for state in d_states:
        state.cities.sort(key=lambda x: x.name)
    d_amenities = list(storage.all("Amenity").values())
    d_amenities.sort(key=lambda x: x.name)
    d_places = list(storage.all("Place").values())
    d_places.sort(key=lambda x: x.name)
    for place in d_places:
        place.description = Markup(place.description)
    Temp = render_template(
        '100-hbnb.html',
        states=d_states,
        amenities=d_amenities,
        places=d_places
    )
    return Temp


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
