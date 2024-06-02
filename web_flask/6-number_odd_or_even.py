#!/usr/bin/python3
"""A script that starts a Flask web application"""
from flask import Flask, render_template

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
    """Displays 'C ' followed by the value of the text variable"""
    modified_text = text.replace("_", " ")
    return f"C {modified_text}"


@app.route("/python/")
@app.route("/python/<text>")
def display_P_text(text="is cool"):
    """Displays 'Python ' followed by the value of the text variable"""
    modified_text = text.replace("_", " ")
    return f"Python {modified_text}"


@app.route("/number/<int:n>")
def display_number(n):
    """Displays the value of n if it is an integer only"""
    return f"{n} is a number"


@app.route("/number_template/<int:n>")
def number_template(n):
    """Displays a HTML page only if n is an integer"""
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>")
def number_odd_or_even(n):
    """Displays a HTML page only if n is an integer"""
    status = "even" if n % 2 == 0 else "odd"
    return render_template("6-number_odd_or_even.html", n=n, status=status)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
