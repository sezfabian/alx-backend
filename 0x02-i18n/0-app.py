#!/usr/bin/env python3
"""
Flask server app module
"""
from flask import Flask, render_template

template_folder = "templates"
app = Flask(__name__)


@app.route("/")
def index():
    """
    Render the index page
    """
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
