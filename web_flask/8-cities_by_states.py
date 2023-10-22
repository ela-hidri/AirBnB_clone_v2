#!/usr/bin/python3
"""  starts a Flask web application """
from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/cities_by_states")
def list_citibystate():
    """display a HTML page"""
    data = storage.all("State")
    return render_template('8-cities_by_states.html', data=data)


@app.teardown_appcontext
def teardown(exc):
    """ remove the current SQLAlchemy Session """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
