from flask import Blueprint, render_template

# split the application into multiple files
views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")