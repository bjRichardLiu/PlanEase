from flask import render_template, Blueprint, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
from .service import createNewSchedule
import numpy as np

schedule = Blueprint('schedule', __name__)

# Global variable to store the intID
intID = 1

@schedule.route('/schedule', methods=['GET', 'POST'])
@login_required
def display_schedule():
    schedule_data = generate_schedule()
    return render_template("schedule.html", schedule=schedule_data)

# The following code is for generating the schedule data

def generate_schedule():
    week, intToTask = createNewSchedule()

    # Prepare the schedule data to be sent to the template
    schedule_data = []
    for i in range(48):
        time = f'{i // 2:02d}:{i % 2 * 30:02d}'
        row_data = {
            'time': time,
            'monday': intToTask[int(week[i, 0])],
            'tuesday': intToTask[int(week[i, 1])],
            'wednesday': intToTask[int(week[i, 2])],
            'thursday': intToTask[int(week[i, 3])],
            'friday': intToTask[int(week[i, 4])],
        }
        schedule_data.append(row_data)

    # Return the schedule data
    return schedule_data

