from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user


# split the application into multiple files
views = Blueprint('views', __name__)

@views.route('/')
@login_required
def home():
    return render_template("home.html")