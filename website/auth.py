from flask import Blueprint, render_template, request, flash

# split the application into multiple files
auth = Blueprint('auth', __name__)

# create a route for the login page
@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return "<h1>Login</h1>"

# create a route for the logout page
@auth.route('/logout')
def logout():
    return "<h1>Logout</h1>"

# create a route for the sign up page
@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        # Basic checks for the input information
        if len(email) < 5:
            flash('Email must be greater than 4 characters.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            # add user to database
            flash('Account created!', category='success')
        
    return "<h1>Sign Up</h1>"