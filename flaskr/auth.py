import functools

from flask import Blueprint
from flask import g
from flask import request
from flask import session
from werkzeug.exceptions import abort
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash

from flaskr.db import get_db

bp = Blueprint("auth", __name__, url_prefix="/auth")


def login_required(view):
    """View decorator that redirects anonymous users to the login page."""

    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            abort(401, "You are not logged in.")

        return view(**kwargs)

    return wrapped_view


@bp.before_app_request
def load_logged_in_user():
    """If a user id is stored in the session, load the user object from
    the database into ``g.user``."""
    user_id = session.get("user_id")

    if user_id is None:
        g.user = None
    else:
        g.user = (
            get_db().execute("SELECT * FROM user WHERE id = ?", (user_id,)).fetchone()
        )


@bp.route("/register", methods=("POST",))
def register():
    """Register a new user.

    Validates that the username is not already taken. Hashes the
    password for security.
    """
    params = request.get_json(force=True)
    username = params["username"]
    password = params["password"]
    db = get_db()

    try:
        db.execute(
            "INSERT INTO user (username, password) VALUES (?, ?)",
            (username, generate_password_hash(password)),
        )
        db.commit()
    except db.IntegrityError:
        # The username was already taken, which caused the
        # commit to fail. Show a validation error.
        abort(400, f"User {username} is already registered.")


@bp.route("/login", methods=("POST",))
def login():
    """Log in a registered user by adding the user id to the session."""
    params = request.get_json(force=True)
    username = params["username"]
    password = params["password"]
    db = get_db()
    user = db.execute(
        "SELECT * FROM user WHERE username = ?", (username,)
    ).fetchone()

    if user is None:
        abort(400, "Incorrect username.")
    elif not check_password_hash(user["password"], password):
        abort(400, "Incorrect password.")

    # store the user id in a new session and return to the index
    session.clear()
    session["user_id"] = user["id"]


@bp.route("/logout")
def logout():
    """Clear the current session, including the stored user id."""
    session.clear()
