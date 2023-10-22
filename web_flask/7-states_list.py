#!/usr/bin/python3
"""  starts a Flask web application """
from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/states_list")
def list_state():
    """display a HTML page"""
    data = storage.all("State")
    return render_template('7-states_list.html', txt='States', data=data)


@app.teardown_appcontext
def teardown(exc):
    """ remove the current SQLAlchemy Session """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
