from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from .models import Task, ReservedTime, WakeUpTime
from . import db
from .service import delete_user_data

# split the application into multiple files
views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        # Drop all tables of the user and accept new data
        delete_user_data()

        # Get the data from the request
        wakeup_time_data = request.form.get('wakeup_time')
        reserved_times_data = [data for data in range(1, 3)]
        tasks_data = [task_data for task_data in range(1, 5)]

        # Save the data in the database
        new_wakeup_time = WakeUpTime(wakeUpTime=wakeup_time_data, user_id=current_user.id)
        db.session.add(new_wakeup_time)

        for reserved_time_data in reserved_times_data:
            new_reserved_time = ReservedTime(user_id=current_user.id, **parse_reserved_time_data(reserved_time_data))
            db.session.add(new_reserved_time)

        for task_data in tasks_data:
            new_task = Task(user_id=current_user.id, **parse_task_data(task_data))
            db.session.add(new_task)

        db.session.commit()

    return render_template("home.html", user=current_user)

def parse_reserved_time_data(data):
    # Parse the data and return a dictionary with the parameters
    # Adjust this function based on your form field names and data types
    parsed_data = {
        'data': request.form.get(f'reserved_time_{data}'),
        'beginTime': request.form.get(f'start_time_{data}'),
        'endTime': request.form.get(f'end_time_{data}'),
    }
    return parsed_data

def parse_task_data(task_data):
    # Parsing individual task data
    # task_data is the index of the task
    # Adjust this function based on your form field names and data types

    # Mapping dictionary for time preference
    time_preference_mapping = {
        'Morning': 0,
        'Afternoon': 1,
        'Evening': 2
    }

    # Extract data for the current task
    task = request.form.get(f'task_name_{task_data}')
    time_required = request.form.get(f'timeRequired_{task_data}')
    deadline = request.form.get(f'deadline_{task_data}')
    morning = request.form.get(f'morning_{task_data}')
    print(task, time_required, deadline, morning)

    # Create the dictionary for the parsed data of the current task
    parsed_data = {
        'data': task,
        'timePreference': time_preference_mapping.get(morning),
        'deadline': deadline,
        'timeRequired': time_required,
    }

    return parsed_data