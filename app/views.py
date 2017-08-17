"""
This renders the views of the application
"""
from flask import render_template
from app import app


@app.route('/', methods=["GET"])
def home():
    """
    This method handles the actions for the default route
    """
    return render_template("login.html")

@app.route('/signup', methods=["GET"])
def signup_page():
    """
    This method handles the actions for the signup GET route
    """
    return render_template("signup.html")
