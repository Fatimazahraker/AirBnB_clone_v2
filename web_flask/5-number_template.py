#!/usr/bin/python3
"""script that starts a Flask web application:"""


from flask import Flask, render_template

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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
