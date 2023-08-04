from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from .models import Task, ReservedTime, WakeUpTime
from . import db


# split the application into multiple files
views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        # HTML needs to get there parameters
        task = request.form.get('task')
        timeRequired = request.form.get('timeRequired')
        priority = request.form.get('priority')
        weekdaysOnly = request.form.get('weekdaysOnly')
        deadline = request.form.get('deadline')
        
        morning = request.form.get('morning')
        
        if len(task) < 1:
            flash('Task is too short!', category='error')
        else:
            newTask = Task(data=task, user_id=current_user.id)
            db.session.add(newTask)
            db.session.commit()
            flash('Task added!', category='success')
            
    return render_template("home.html", user=current_user)