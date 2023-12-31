from flask import Blueprint, render_template, request, flash, redirect, url_for
from . import db
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user

# split the application into multiple files
auth = Blueprint('auth', __name__)

# create a route for the login page
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('logemail')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        # Basic checks for the input information
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists :/', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        else:
            new_user = User(email = email, firstName = first_name, password = generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))
        
        
        
        
        
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                print("trying to login")
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again :(', category='error')
        else:
            flash('Email does not exist, please create an account.', category='error')
        
    return render_template("login.html", user=current_user)

# create a route for the logout page
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

"""
# create a route for the sign up page
@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('first_name')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        # Basic checks for the input information
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists :/', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        else:
            new_user = User(email = email, firstName = first_name, password = generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))
        
    return render_template("sign_up.html", user=current_user)
"""