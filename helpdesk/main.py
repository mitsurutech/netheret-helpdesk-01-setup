"""General pages that do not belong to one feature."""
from flask import Blueprint

bp = Blueprint("main", __name__)


@bp.route("/")
def home():
    # For now we return a little HTML as a string, just to prove the app runs.
    # The next step moves the HTML into templates.
    return "<h1>Netheret help desk</h1><p>The app is running.</p>"
