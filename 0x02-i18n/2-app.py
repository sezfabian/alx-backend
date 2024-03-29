#!/usr/bin/env python3
"""
Flask server app module
"""
from flask import Flask, render_template, request
from flask_babel import Babel

template_folder = "templates"
app = Flask(__name__)
babel = Babel(app)


class Config:
    """
    Configuration class for Babel
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


@babel.localeselector
def get_locale():
    """
    Get the selected language
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


app.config.from_object(Config)


@app.route("/")
def index():
    """
    Render the index page
    """
    return render_template("2-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
