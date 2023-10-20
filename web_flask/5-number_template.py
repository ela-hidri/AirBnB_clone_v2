#!/usr/bin/python3
""" starts a Flask web application """
from flask import Flask
from flask import abort
from flask import render_template
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello_hbnb():
    """ display Hello """
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """ display HBNB """
    return "HBNB"


@app.route("/c/<text>")
def c_text(text):
    """display “C ” followed by the value of the text"""
    return "C {}".format(text.replace('_', ' '))


@app.route('/python', defaults={'text': 'is cool'})
@app.route("/python/<text>")
def py_text(text):
    """ display “Python ”, followed by the value of the text"""
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>')
def numb(n):
    """ diplay n is number if integer """
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>')
def nb_tmp(n):
    """render template"""
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
