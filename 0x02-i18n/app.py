#!/usr/bin/env python3
"""
Flask server app module
"""
from flask import Flask, g, render_template, request
from flask_babel import Babel, _
from typing import Dict, Union

template_folder = "templates"
app = Flask(__name__)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """
    Configuration class for Babel
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    if 'locale' in request.args and request.args['locale'] \
                in app.config['LANGUAGES']:
        if request.args['locale'] in app.config['LANGUAGES']:
            return request.args['locale']
    elif g.user:
        locale = g.user.get('locale')
        if locale in app.config['LANGUAGES']:
            return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user() -> Union[Dict, None]:
    """
    Returns a user dictionary or None if the ID cannot be found
    or if login_as was not passed
    """
    user_id = request.args.get('login_as')

    if user_id:
        return users.get(int(user_id))

    return None


@app.before_request
def before_request():
    """
    Uses get_user to find a user if any, and set it as a global on flask.g.user
    """
    g.user = get_user()


@app.route("/")
def index():
    """
    Render the index page
    """
    if g.user:
        username = g.user['name']
    else:
        username = None
    return render_template('5-index.html', username=username)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
