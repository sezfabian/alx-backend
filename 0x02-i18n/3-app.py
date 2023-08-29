#!/usr/bin/env python3
"""
Flask server app module
"""
from flask import Flask, render_template, request
from flask_babel import Babel, _

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
    home_title = _("Welcome to Holberton")
    home_header = _("Hello world")
    return render_template("3-index.html",
                           home_title=home_title, home_header=home_header)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
