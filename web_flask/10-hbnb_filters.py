#!/usr/bin/python3
"""script that starts a Flask web application:"""


from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """display hello"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """display hello"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """ despaly text"""
    text = text.replace('_', ' ')
    return "C " + text


@app.route('/python/')
@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is cool'):
    """ despaly text"""
    text = text.replace('_', ' ')
    return "Python " + text


@app.route('/number/<int:n>', strict_slashes=False)
def number_isinteger(n):
    """ despaly number"""
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n=None):
    """ despaly HTML page"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n=None):
    """ despaly HTML page"""
    if n % 2 == 0:
        result = "even"
    else:
        result = "odd"
    return render_template('6-number_odd_or_even.html', result=result, n=n)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ def doc """
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """ def doc """
    states = storage.all(State)
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def close(error):
    """ def doc """
    storage.close()


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states(id=None):
    """ Route function for /states and /states/<id> """
    not_found = False
    if id is not None:
        states = storage.all(State, id)
        with_id = True
        if len(states) == 0:
            not_found = True
    else:
        states = storage.all(State)
        with_id = False
    return render_template('9-states.html', states=states,
                           with_id=with_id, not_found=not_found)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb2():
    """ Route function for /states and /states/<id> """
    amenities = storage.all(Amenity)
    states = storage.all(State)
    return render_template('10-hbnb_filters.html', states=states, amenities=amenities)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
