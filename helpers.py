from flask import session
from cs50 import SQL
db = SQL("sqlite:///final.db")


def format_number(n):
    """Format n as a string with at least 8 digits, padding with leading zeros if necessary."""
    return f"{n:08}"


def select_your_highscore():
    """ Selects the user's current high score depending on whether the user is logged in or not """

    if session.get("user_id") is None:
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", "PLAYER"
        )
        # If PLAYER does not exist yet
        if len(rows) == 0:
            your_highscore = 0
        # If PLAYER already exists
        else:
            your_highscore = rows[0]["highscore"]
    else:
        rows = db.execute(
            "SELECT highscore FROM users WHERE id = ?", session["user_id"]
        )
        your_highscore = rows[0]["highscore"]

    return your_highscore


def select_your_name():
    """ Selects the user's name, if not logged in it's PLAYER """

    if session.get("user_id") is None:
        username = "PLAYER"
    else:
        rows = db.execute(
            "SELECT username FROM users WHERE id = ?", session["user_id"]
        )
        username = rows[0]["username"]

    return username
