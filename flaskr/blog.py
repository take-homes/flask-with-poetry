from flask import Blueprint, Response, g, request
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint("blog", __name__)


@bp.route("/")
def index():
    """Show all the posts, most recent first."""
    db = get_db()
    posts = db.execute(
        "SELECT p.id, title, body, created, author_id, username"
        " FROM post p JOIN user u ON p.author_id = u.id"
        " ORDER BY created DESC"
    ).fetchall()
    return [{
      "title": post["title"],
      "body": post["body"],
      "created": post["created"],
      "author_id": post["author_id"],
      "username": post["username"],
    } for post in posts]


def get_post(id, check_author=True):
    """Get a post and its author by id.

    Checks that the id exists and optionally that the current user is
    the author.

    :param id: id of post to get
    :param check_author: require the current user to be the author
    :return: the post with author information
    :raise 404: if a post with the given id doesn't exist
    :raise 403: if the current user isn't the author
    """
    post = (
        get_db()
        .execute(
            "SELECT p.id, title, body, created, author_id, username"
            " FROM post p JOIN user u ON p.author_id = u.id"
            " WHERE p.id = ?",
            (id,),
        )
        .fetchone()
    )

    if post is None:
        abort(404, f"Post id {id} doesn't exist.")

    if check_author and post["author_id"] != g.user["id"]:
        abort(403)

    return {
      "title": post["title"],
      "body": post["body"],
      "created": post["created"],
      "author_id": post["author_id"],
      "username": post["username"],
    }


@bp.route("/create", methods=("POST",))
@login_required
def create():
    """Create a new post for the current user."""
    params = request.get_json(force=True)
    title = params["title"]
    body = params["body"]

    db = get_db()
    db.execute(
        "INSERT INTO post (title, body, author_id) VALUES (?, ?, ?)",
        (title, body, g.user["id"]),
    )
    db.commit()
    return Response(status=200)


@bp.route("/<int:id>/update", methods=("POST",))
@login_required
def update(id):
    """Update a post if the current user is the author."""
    post = get_post(id)

    params = request.get_json(force=True)
    title = params["title"]
    body = params["body"]

    db = get_db()
    db.execute(
        "UPDATE post SET title = ?, body = ? WHERE id = ?", (title, body, id)
    )
    db.commit()
    return Response(status=200)


@bp.route("/<int:id>/delete", methods=("POST",))
@login_required
def delete(id):
    """Delete a post.

    Ensures that the post exists and that the logged in user is the
    author of the post.
    """
    get_post(id)
    db = get_db()
    db.execute("DELETE FROM post WHERE id = ?", (id,))
    db.commit()
    return Response(status=200)
