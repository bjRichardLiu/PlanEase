from flask import Blueprint

# split the application into multiple files
views = Blueprint('views', __name__)

@views.route('/')
def home():
    return "<h1>Home</h1>"