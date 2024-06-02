#!/usr/bin/python3
"""A script that starts a Flask web application"""
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello_hbnb():
    """Displays Hello HBNB!"""
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """Displays HBNB"""
    return "HBNB"


@app.route("/c/<text>")
def display_text(text):
    """Displays Html text"""
    for ch in text:
        if ch == "_":
            text = text.replace("_", " ")
    return text


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
