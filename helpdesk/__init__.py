"""The Netheret help desk web app.

create_app() builds the Flask app. Flask looks for a function with this
name when you run `flask --app helpdesk run`.
"""
from flask import Flask


def create_app():
    app = Flask(__name__)

    # Each part of the app is a blueprint: a group of pages in its own file.
    from . import main
    app.register_blueprint(main.bp)

    return app
