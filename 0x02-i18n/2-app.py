  1 #!/usr/bin/env python3
  2 """
  3 Flask server app module
  4 """
  5 from flask import Flask, render_template
  6 from flask_babel import Babel
  7 
  8 template_folder = "templates"
  9 app = Flask(__name__)
 10 babel = Babel(app)
 11 
 12 
 13 class Config:
 14     """
 15     Configuration class for Babel
 16     """
 17     LANGUAGES = ["en", "fr"]
 18     BABEL_DEFAULT_LOCALE = "en"
 19     BABEL_DEFAULT_TIMEZONE = "UTC"
 20 
 21 
 22 @babel.localeselector
 23 def get_locale():
 24     """
 25     Get the selected language
 26     """
 27     return request.accept_languages.best_match(app.config['LANGUAGES'])
 28 
 29        
 30 app.config.from_object(Config)
 31 
 32 
 33 @app.route("/")
 34 def index():
 35     """
 36     Render the index page
 37     """
 38     return render_template("1-index.html")
 39 
 40 
 41 if __name__ == "__main__":
 42     app.run(host="0.0.0.0", port=5000, debug=True)
