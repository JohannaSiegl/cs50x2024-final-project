import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, jsonify
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import format_number, select_your_highscore, select_your_name


""" from helpers import # names of functions in helpers """

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters['format_number'] = format_number

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///final.db")

# Global variable to score the user's high score
global_score = 0

# Handle POST request for variable score
@app.route('/save-score', methods=['POST'])
def save_score():
    global global_score
    data = request.get_json()
    global_score = data['score']

    # Safe the high score in the database
    # When user is not logged in
    if session.get("user_id") is None:
        print("User is not logged in")
        # Query database for PLAYER
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", "PLAYER"
        )
        # If PLAYER does not exist yet
        if len(rows) == 0:
            print("PLAYER does not exist, creating new entry")
            # Add PLAYER and score to database
            db.execute(
                "INSERT INTO users (username, hash, highscore) VALUES (?, ?, ?)", "PLAYER", "x", global_score
            )
        # If PLAYER already exists, check whether score > highscore and update highscore if needed
        else:
            print("PLAYER exists, checking highscore")
            highscore = rows[0]["highscore"]
            if global_score > highscore:
                db.execute(
                    "UPDATE users SET highscore = ? WHERE username = ?", global_score, "PLAYER"
                )
    else:
        # When user is logged in, check whether score > highscore and update highscore if needed
        rows = db.execute(
            "SELECT highscore FROM users WHERE id = ?", session["user_id"]
        )
        highscore = rows[0]["highscore"]
        if global_score > highscore:
            db.execute(
                "UPDATE users SET highscore = ? WHERE id = ?", global_score, session["user_id"]
            )

    # Indicate success
    return jsonify(success=True)



@app.route("/high-scores")
def highscores():
    """Shows high scores from database"""

    # SELECT your high score
    your_highscore = select_your_highscore()

    # SELECT data from database to display
    highscores = db.execute("SELECT * FROM users ORDER BY highscore DESC LIMIT 10")
    return render_template("high-scores.html", your_highscore=your_highscore, highscores=highscores)


@app.route("/")
def index():
    """Title Page"""

    # SELECT your username
    your_username = select_your_name()

    # SELECT your high score
    your_highscore = select_your_highscore()

    return render_template("index.html", is_index=True, your_username=your_username, your_highscore=your_highscore, global_score=global_score)


@app.route("/info")
def info():
    """Information about the binary system"""

    return render_template("info1.html")


@app.route("/password", methods=["GET", "POST"])
def password():
    """Set username and password"""

    global global_score

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        username = request.form.get('username')
        password = request.form.get('password')

        # Ensure username and password was submitted
        if not username or not password:
            flash('PLEASE ENTER A VALID USERNAME AND PASSWORD!')
            return render_template("password.html")

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", username
        )

        # If username does not exist yet
        if len(rows) == 0:

            # Generate a hash of the password
            hash = generate_password_hash(password, method='pbkdf2', salt_length=16)

            # Add user to database
            db.execute(
                "INSERT INTO users (username, hash) VALUES (?, ?)", username, hash
            )

            # Query database for username (again)
            rows = db.execute(
                "SELECT * FROM users WHERE username = ?", username
            )

            # Log user in
            session["user_id"] = rows[0]["id"]

        # If username already exists, check for correct password
        if len(rows) == 1 and not check_password_hash(
            rows[0]["hash"], password
        ):
            flash('PASSWORD IS INCORRECT OR USERNAME IS ALREADY TAKEN!')
            return render_template("password.html")

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        # Log current user out by forgetting any user_id
        session.clear()

        # Reset latest score
        global_score = 0

        return render_template("password.html")


@app.route("/start")
def start():
    """Start playing the game"""

    return render_template("start.html", is_start=True)

    # For storing the currend high score in the db, see save_score() above

if __name__ == '__main__':
    app.run(debug=True)



